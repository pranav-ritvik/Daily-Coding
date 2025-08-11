#include <limits.h>

int maxProfit(int* prices, int pricesSize) {
    int minPrice = INT_MAX;
    int best = 0;
    for (int i = 0; i < pricesSize; i++) {
        if (prices[i] < minPrice) minPrice = prices[i];
        int profit = prices[i] - minPrice;
        if (profit > best) best = profit;
    }
    return best;
}
