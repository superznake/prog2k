class BinaryTreeException(Exception):
    """
    Basic class for binary tree exceptions
    """

class HeightSubZeroError(BinaryTreeException):
    """
    Class for height below zero
    """

class ZeroRootMultiplyErrror(BinaryTreeException):
    """
    Class for zero root multiplying
    """

class LambdaException(BinaryTreeException):
    """
    Basic class for lamdas exceptions
    """

class NullLambdaError(LambdaException):
    """
    Class for unassigned functions transfer
    """

class WrongLamdaError(LambdaException):
    """
    Class for wrong functions trnsfer
    """