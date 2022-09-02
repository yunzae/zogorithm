#include <stdio.h>
#define MIN(x, y) ((x) > (y) ? (y) : (x))
#include <stdlib.h>
#include <string.h>
#include <limits.h>

struct Food
{
    int p;
    int f;
    int s;
    int v;
    int index;
    int price;
};



struct Food food_min;
struct Food foods[50 + 1];
int recipe[50 + 1], recipeLength;
int answer[50 + 1], answerLength;
int visit[50 + 1];
int lowerBound = INT_MAX;
int nutrientSum = 0;
int input_num;

int recipeCmp(const int* recipe1, int recipe1Length, const int* recipe2, int recipe2Length)
{
    const int minLength = MIN(recipe1Length, recipe2Length);

    for (int i = 0; i < minLength; ++i)
    {
        if (recipe1[i] < recipe2[i])
            return 1;
        if (recipe1[i] > recipe2[i])
            return -1;
    }

    if (recipe1Length < recipe2Length)
        return 1;
    if (recipe1Length > recipe2Length)
        return -1;
    return 0;
}
void cut(int depth, struct Food food)
{
    struct Food newFood = food;
    newFood.f += foods[depth].f;
    newFood.p += foods[depth].p;
    newFood.s += foods[depth].s;
    newFood.v += foods[depth].v;
    newFood.price += foods[depth].price;

    if (newFood.f >= 0 && newFood.p >= 0 && newFood.s >= 0 && newFood.v >= 0)
    {
        recipe[recipeLength++] = foods[depth].index + 1;

        const int newBound = newFood.price;
        const int newNutrientSum = newFood.p + newFood.f + newFood.s + newFood.v;

        if (lowerBound > newBound || (lowerBound == newBound && ((newNutrientSum > nutrientSum) ||
            (newNutrientSum == nutrientSum && recipeCmp(answer, answerLength, recipe, recipeLength)))))
        {
            memcpy(answer, recipe, sizeof(int) * recipeLength);
            answerLength = recipeLength;
            lowerBound = newBound;
            nutrientSum = newNutrientSum;
        }

        --recipeLength;
    }

    if (depth == input_num - 1)
        return;

    if (newFood.price <= lowerBound)
    {
        recipe[recipeLength++] = foods[depth].index + 1;
        cut(depth + 1, newFood);
        --recipeLength;
    }

    cut(depth + 1, food);
}

int initialCmp(const void* pfood1, const void* pfood2)
{
    struct Food food1 = *(struct Food*)pfood1;
    struct Food food2 = *(struct Food*)pfood2;

    double ratio1 = (food1.p * 1000000000LL + food1.f * 1000000LL + food1.s * 1000LL + food1.v) / (double)(food1.price + 1);
    double ratio2 = (food2.p * 1000000000LL + food2.f * 1000000LL + food2.s * 1000LL + food2.v) / (double)(food2.price + 1);

    if (ratio1 < ratio2)
        return 1;

    if (ratio1 > ratio2)
        return -1;

    return 0;
}

int answerCmp(const void* p1, const void* p2)
{
    int n1 = *(int*)p1;
    int n2 = *(int*)p2;

    if (n1 < n2)
        return -1;

    if (n1 > n2)
        return 1;

    return 0;
}



int main()
{
    scanf("%d %d %d %d %d", &input_num, &food_min.p, &food_min.f, &food_min.s, &food_min.v);
    food_min.p = -food_min.p;
    food_min.f = -food_min.f;
    food_min.s = -food_min.s;
    food_min.v = -food_min.v;

    for (int i = 0; i < input_num; ++i)
    {
        struct Food* food = &foods[i];
        scanf("%d %d %d %d %d", &food->p, &food->f, &food->s, &food->v, &food->price);
        food->index = i;
    }
    qsort(foods, input_num, sizeof(struct Food), initialCmp);
    cut(0, food_min);
    if (answerLength != 0)
    {
        qsort(answer, answerLength, sizeof(int), answerCmp);
        for (int i = 0; i < answerLength; ++i)
            printf("%d ", answer[i]);
    }
    else
    {
        printf("0");
    }

    return 0;
}

