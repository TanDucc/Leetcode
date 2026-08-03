#include <stdio.h>

int maxProfit(int* prices, int pricesSize) {
    
    int left = 0;
    int right = 1;
    int maxProfit = 0;

    while (right < pricesSize) {
        if (prices[left] < prices[right]) {
            int profit = prices[right] - prices[left];
            if (profit > maxProfit) {
                maxProfit = profit;

            }
        } else {
            left = right;
        }
        right++;
    }    
    return maxProfit;
}