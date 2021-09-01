"""Relational Operators"""
__author__ = "730407702"

left_hand_side: str = input("Left hand side: ")
right_hand_side: str = input("Right hand side: ")
less_than_response: bool = int(left_hand_side) < int(right_hand_side)
print(left_hand_side + " < " + right_hand_side + " is " + str(less_than_response))
at_least_response: bool = int(left_hand_side) >= int(right_hand_side)
print(left_hand_side + " >= " + right_hand_side + " is " + str(at_least_response))
equal_response: bool = int(left_hand_side) == int(right_hand_side)
print(left_hand_side + " == " + right_hand_side + " is " + str(equal_response))
not_equal_response: bool = int(left_hand_side) != int(right_hand_side)
print(left_hand_side + " != " + right_hand_side + " is " + str(not_equal_response))