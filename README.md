# Delivery Man

DeliveryMan1 and DeliveryMan2 are the only two delivery men of FoodDelivery store. On this day, the store received N orders. It's known that the amount of tips may be different when handled by different delivery man. More specifically, if DeliveryMan1 takes the ith order, he would be tipped DM1i rupees and if DeliveryMan2 takes this order, the tip would be DM2i rupees.

They decided that they would distribute the orders among themselves to maximize the total tip money. One order will be handled by only one person. Also, due to time constraints DeliveryMan1 cannot take more than X orders and DeliveryMan2 cannot take more than Y orders. It is guaranteed that X + Y is greater than or equal to N, which means that all the orders can be handled by either DeliveryMan1 or DeliveryMan2 .

Please find out the maximum possible amount of total tip money after processing all the orders.

## Input:

The first line contains three integers N, X, Y.

The second line contains N integers. The ith integer represents DM1i.

The third line contains N integers. The ith integer represents DM2i.

## Output: 

Print the integer representing the maximum tip money they would receive.

## Constraints

1 ≤ N ≤ 15

1 ≤ X, Y ≤ N; X + Y ≥ N

1 ≤ DM1i, DM2i ≤ 100

## Example

### Input:

8 6 6

1 2 3 4 5 6 7 8

8 7 6 5 4 3 2 1

### Output:

52
