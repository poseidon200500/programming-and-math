#include <stdio.h>
#include <math.h>
//сортировка пузырьком
void BubbleSort(int *arr, int len)  //работает корректно
{
    for(int i = 0; i < len-1; i++){
        for (int j = 0; j < (len-1-i); j++){
            if (arr[j] > arr[j+1]){
                int k = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = k;
            }
        }
    }
}
//шейкерная сортировка(вариация сортировки пузырьком)
void ShakerSort(int *arr, int len)  //работает корректно
{
    int begin = 0;
    int end = len-1;
    while((end-begin) > 1){
        for (int i = begin; i < (end-1); i++){
            if (arr[i] > arr[i+1]){
                int k = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = k;
            }
        }
        end -= 1;
        for (int i = end; i < (begin+1); i-=1){
            if (arr[i] < arr[i-1]){
                int k = arr[i];
                arr[i] = arr[i-1];
                arr[i-1] = k;
            }
        begin += 1;
        }
    }
}
//сортировка расчёской(вариация сортировки пузырьком)
void CombSort(int *arr, int len) //
{
    int range = roundf(len/1.247);
    while (range > 1){
        for (int i = 0; (i+range) < len-1; i++){
            if (arr[i] > arr[i+range]){
                int k = arr[i+range];
                arr[i+range] = arr[i];
                arr[i] = k;
            }
        }
        range = range/1.247;
    }
}
//сортировка перестановками
void PerestanSort(int *arr, int len) //работает корректно
{

    for (int i = 0; i < len; i++){
        int ind = 0;
        int max = arr[0];
        //поиск максимального элемента подстроки
        for (int j = 1; j< len-i; j++)
            if (arr[j] > max){
                max = arr[j];
                ind = j;
            }
        //поменять местами максимум и ещё не отсортированный элемент с конца
        arr[ind] = arr[len-1-i];
        arr[len-1-i] = max;
    }
}

void QuickSort()
{

}

void pivot(int *arr, int left, int right) // left = 0, right = N
{
    if ((right - left) > 1)
    {
        //алгоритм сортировки
        int ser = arr[left];
        int ind = left;
        
        for (int i = left; i < right; i++){
            if (arr[i] < ser){
                int k = arr[ind];
                arr[ind] = arr[i];
                arr[i] = k;
                ind++;
            }
        }
        //если есть несколько серединных элементов
        int ind2 = ind;
        for(int i = ind; i < right; i++){
            if (arr[i] == arr[ind])
                ind2 = i;
            else
                break;
        }
        //запускаем рекурсию на левый и правый подотрезки
        pivot(arr,left,ind);
        pivot(arr,ind2,right);
    }
}

int main(){
    //инициализация переменных
    int mass[20] = {0};
    //int mass2[20] = {0};
    int N = 0;
    //заполнение массива
    scanf("%d",&N);
    for (int i = 0; i < N; i++)
        scanf("%d", &mass[i]);
    //сортировка массива
    pivot(mass,0,N);
    //вывод массива
    for (int i = 0; i < N; i++)
        printf("%d ",mass[i]);

    return 0;
}
