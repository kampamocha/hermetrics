from .metric import Metric

class Jaro(Metric):

    def __init__(self, name='Jaro'):
        super().__init__(name=name)

    def similarity(self, source, target, cost=1):
        """Jaro similarity"""
        s_len = len(source)
        t_len = len(target)

        if s_len == 0 and t_len == 0:
            return 1

        s_idx = [False] * s_len
        t_idx = [False] * t_len

        # m = matches, d = neighborhood distance
        m = 0
        d = max(s_len, t_len) // 2 - 1

        for i in range(s_len):
            left = max(0, i-d)
            right = min(i+d+1, t_len)

            for j in range(left, right):
                if t_idx[j]:
                    continue
                if source[i] == target[j]:
                    s_idx[i] = True
                    t_idx[j] = True
                    m += 1
                    break

        if m == 0:
            return 0

        s_tokens = [source[i] for i in range(s_len) if s_idx[i]]
        t_tokens = [target[i] for i in range(t_len) if t_idx[i]]

        # t = transpositions
        t = sum([s != t for s,t in zip(s_tokens, t_tokens)]) / 2

        return ( m / s_len + m / t_len + (m - t) / m ) / 3

    def distance(self, source, target, cost=1):
        """Jaro distance"""
        return 1 - self.similarity(source, target, cost)

if(__name__ == '__main__'):
    print("Jaro similarity")
