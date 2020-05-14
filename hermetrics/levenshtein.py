from .metric import Metric

class Levenshtein(Metric):

    def __init__(self, name='Levenshtein'):
        super().__init__(name=name)

    def distance(self, source, target, cost=(1,1,1)):
        """Levenshtein distance with costs for deletion, insertion and substitution"""
        s_len = len(source)
        t_len = len(target)

        if type(cost) == int or type(cost) == float:
            del_cost = ins_cost = sub_cost = cost
        else:
            del_cost, ins_cost, sub_cost = cost

        rows = s_len + 1
        cols = t_len + 1
        D = [[0 for j in range(cols)] for i in range(rows)]

        # source prefixes can be transformed into empty strings
        # by deletions:
        for i in range(1, rows):
            D[i][0] = i * del_cost
        # target prefixes can be created from an empty source string
        # by inserting the characters
        for j in range(1, cols):
            D[0][j] = j * ins_cost

        for j in range(1, cols):
            for i in range(1, rows):
                deletion = D[i-1][j] + del_cost
                insertion = D[i][j-1] + ins_cost
                substitution_or_equal = D[i-1][j-1]
                if source[i-1] != target[j-1]:
                    substitution_or_equal += sub_cost

                D[i][j] = min(deletion, insertion, substitution_or_equal)

        return D[-1][-1]

    def max_distance(self, source, target, cost=(1,1,1)):
        """Levenshtein maximum distance value"""
        s_len = len(source)
        t_len = len(target)

        if type(cost) == int or type(cost) == float:
            del_cost = ins_cost = sub_cost = cost
        else:
            del_cost, ins_cost, sub_cost = cost

        max_del = max(s_len - t_len, 0)
        max_ins = max(t_len - s_len, 0)
        max_sub = min(s_len, t_len)

        return max_del*del_cost + max_ins*ins_cost + max_sub*sub_cost


if(__name__ == '__main__'):
    print("Levenshtein distance")

#%% Rectified Levenshtein

class RectifiedLevenshtein(Levenshtein):

    def __init__(self, name='Rectified Levenshtein'):
        super().__init__(name=name)

    def distance(self, source, target, cost=(1,1,1), threshold=None):
        """Levenshtein distance with costs for deletion, insertion and substitution"""
        s_len = len(source)
        t_len = len(target)

        if type(cost) == int or type(cost) == float:
            del_cost = ins_cost = sub_cost = cost
        else:
            del_cost, ins_cost, sub_cost = cost

        #  If threshold is not defined then go all the way
        if threshold == None:
            threshold = self.max_distance(source, target, cost)

        # You need at least s_len - t_len deletions
        if (s_len - t_len) * del_cost > threshold:
            return self.max_distance(source, target, cost)
        # You need at least t_len - s_len insertions
        if (t_len - s_len) * ins_cost > threshold:
            return self.max_distance(source, target, cost)

        rows = s_len + 1
        cols = t_len + 1
        D = [[0 for j in range(cols)] for i in range(rows)]

        # source prefixes can be transformed into empty strings
        # by deletions:
        for i in range(1, rows):
            D[i][0] = i * del_cost
        # target prefixes can be created from an empty source string
        # by inserting the characters
        for j in range(1, cols):
            D[0][j] = j * ins_cost

        for j in range(1, cols):
            for i in range(1, rows):
                deletion = D[i-1][j] + del_cost
                insertion = D[i][j-1] + ins_cost
                substitution_or_equal = D[i-1][j-1]
                if source[i-1] != target[j-1]:
                    substitution_or_equal += sub_cost

                D[i][j] = min(deletion, insertion, substitution_or_equal)

            # Early stopping if threshold is reached
            current_column = [row[j] for row in D]
            if min(current_column) > threshold:
                #print("Early stopping")
                return self.max_distance(source, target, cost)

        # If threshold is reached on last column return max_distance for consistency
        if D[-1][-1] > threshold:
            #print("Last column")
            return self.max_distance(source, target, cost)

        return D[-1][-1]

    def normalized_distance(self, source, target, cost=1, threshold=1):
        """Normalized distance between two objects"""
        # Threshold must be in [0,1] range
        clamped_threshold = self.normalize(threshold, 0, 1)
        distance_threshold = clamped_threshold * self.max_distance(source, target, cost)
        return self.normalize(self.distance(source, target, cost, distance_threshold), self.min_distance(source, target, cost), self.max_distance(source, target, cost))

    def similarity(self, source, target, cost=1, threshold=0):
        """Normalized similarity between two objects"""
        clamped_inverse_threshold = 1 - self.normalize(threshold, 0, 1)
        return 1 - self.normalized_distance(source, target, cost, clamped_inverse_threshold)
