"""Numeric Operators"""
__author__ = "730407702"

left_hand_side: str = input("Left-hand side: ")
right_hand_side: str = input("Right-hand side: ")
exponent_response: int = int(left_hand_side)**int(right_hand_side)
print(left_hand_side + " ** " + right_hand_side + " is " + str(exponent_response))
division_response: float = int(left_hand_side)/int(right_hand_side)
print(left_hand_side + " / " + right_hand_side + " is " + str(division_response))
integer_division_response: int = int(left_hand_side)//int(right_hand_side)
print(left_hand_side + " // " + right_hand_side + " is " + str(integer_division_response))
remainder_response: int = int(left_hand_side)%int(right_hand_side)
print(left_hand_side + " % " + right_hand_side + " is " + str(remainder_response))