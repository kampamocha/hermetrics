class Metric:
    """Class for metric implementations"""

    def __init__(self, distance=None, max_distance=None, min_distance=None, normalize=None, normalized_distance=None,  similarity=None, name='Generic'):
        """Class constructor - receives functions for distance or similarity evaluation"""
        self.name = name
        if distance:
            self.distance = distance
        if max_distance:
            self.max_distance = max_distance
        if min_distance:
            self.min_distance = min_distance
        if normalize:
            self.normalize = normalize
        if normalized_distance:
            self.normalized_distance = normalized_distance
        if similarity:
            self.similarity = similarity

    def __repr__(self):
        """Class representation"""
        return f'Metric({self.name!r})'

    # Default methods
    def distance(self, source, target, cost=1):
        """Default distance function, 0 for equal, 1 for not equal"""
        return 0 if source == target else 1

    def max_distance(self, source, target, cost=1):
        """Maximum distance value"""
        if len(source) == 0 and len(target) == 0:
            return 0
        return 1

    def min_distance(self, source, target, cost=1):
        """Minimum distance value"""
        return 0

    def normalize(self, x, low=0, high=1):
        """Function for value normalization"""
        if high <= low:
            return 0
        if x >= high:
            return 1
        if x <= low:
            return 0
        return (x - low) / (high - low)

    def normalized_distance(self, source, target, cost=1):
        """Normalized distance between two objects"""
        return self.normalize(self.distance(source, target, cost), self.min_distance(source, target, cost), self.max_distance(source, target, cost))

    def similarity(self, source, target, cost=1):
        """Normalized similarity between two objects"""
        return 1 - self.normalized_distance(source, target, cost)


if(__name__ == '__main__'):
    print("hermetrics is similar but different")
