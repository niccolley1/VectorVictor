import math
from LinearAlgebra import LinearAlgebra, ShapeError
from LinearAlgebra import *
from nose.tools import raises


def are_equal(x, y, tolerance=0.001):
    """Helper function to compare floats, which are often not quite equal."""
    return abs(x - y) <= tolerance


m = [3, 4]
n = [5, 0]

v = [1, 3, 0]
w = [0, 2, 4]
u = [1, 1, 1]
y = [10, 20, 30]
z = [0, 0, 0]


def test_shape_vectors():
    f = LinearAlgebra()
    """shape takes a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns. (num_rows, num_col)
    (for a matrix.)"""
    assert f.shape([1]) == (1,)
    assert f.shape(m) == (2,)
    assert f.shape(v) == (3,)

def test_vector_add():
    f = LinearAlgebra()

    """
    [a b]  + [c d]  = [a+c b+d]
    Matrix + Matrix = Matrix
    """
    assert f.vector_add(v, w) == [1, 5, 4]
    assert f.vector_add(u, y) == [11, 21, 31]
    assert f.vector_add(u, z) == u


def test_vector_add_is_commutative():
    f = LinearAlgebra()
    assert f.vector_add(w, y) == f.vector_add(y, w)


@raises(ShapeError)
def test_vector_add_checks_shapes():
    f = LinearAlgebra()
    """Shape rule: the vectors must be the same size."""
    f.vector_add(m, v)


def test_vector_sub():
    """
    [a b]  - [c d]  = [a-c b-d]
    Matrix + Matrix = Matrix
    """
    f = LinearAlgebra()
    assert f.vector_sub(v, w) == [1, 1, -4]
    assert f.vector_sub(w, v) == [-1, -1, 4]
    assert f.vector_sub(y, z) == y
    assert f.vector_sub(w, u) == f.vector_sub(z, f.vector_sub(u, w))


@raises(ShapeError)
def test_vector_sub_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    f = LinearAlgebra()
    f.vector_sub(m, v)


def test_vector_sum():
    f = LinearAlgebra()

    """vector_sum can take any number of vectors and add them together."""
    assert f.vector_sum(v, w, u, y, z) == [12, 26, 35]


# @raises(ShapeError)
# def test_vector_sum_checks_shapes():
#     """Shape rule: the vectors must be the same size."""
#     vector_sum(v, w, m, y)
    #
    #
    # def test_dot():
    #     """
    #     dot([a b], [c d])   = a * c + b * d
    #     dot(Vector, Vector) = Scalar
    #     """
    #     assert dot(w, y) == 160
    #     assert dot(m, n) == 15
    #     assert dot(u, z) == 0
    #
    #
    # @raises(ShapeError)
    # def test_dot_checks_shapes():
    #     """Shape rule: the vectors must be the same size."""
    #     dot(v, m)
    #
    #
    # def test_vector_multiply():
    #     """
    #     [a b]  *  Z     = [a*Z b*Z]
    #     Vector * Scalar = Vector
    #     """
    #     assert vector_multiply(v, 0.5) == [0.5, 1.5, 0]
    #     assert vector_multiply(m, 2) == [6, 8]
    #
    #
    # def test_vector_mean():
    #     """
    #     mean([a b], [c d]) = [mean(a, c) mean(b, d)]
    #     mean(Vector)       = Vector
    #     """
    #     assert vector_mean(m, n) == [4, 2]
    #     assert vector_mean(v, w) == [0.5, 2.5, 2]
    #     assert are_equal(vector_mean(v, w, u)[0], 2 / 3)
    #     assert are_equal(vector_mean(v, w, u)[1], 2)
    #     assert are_equal(vector_mean(v, w, u)[2], 5 / 3)
    #
    #
    # def test_magnitude():
    #     """
    #     magnitude([a b])  = sqrt(a^2 + b^2)
    #     magnitude(Vector) = Scalar
    #     """
    #     assert magnitude(m) == 5
    #     assert magnitude(v) == math.sqrt(10)
    #     assert magnitude(y) == math.sqrt(1400)
    #     assert magnitude(z) == 0
    #
    #

