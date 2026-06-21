def merge_sort(list_to_sort):
    """ Die Funktion merge_sort nimmt eine Liste als Argument und sortiert sie mit dem merge sort Algorithmus.
    
    Input: Liste mit Integern
    """
    
    # Listen der Länge eins sind sortiert
    if len(list_to_sort) > 1:
        # Teilt die Liste in zwei möglichst gleichgroße Listen auf.
        mid = len(list_to_sort) // 2
        left = list_to_sort[:mid]
        right = list_to_sort[mid:]
        
        # Sortiert die Listen rekursiv mit merge_sort
        merge_sort(left)
        merge_sort(right)

        l = 0
        r = 0
        i = 0
        
        # Fügt die sortierten Listen "left" und "right" zu einer gesamten sortierten Liste zusammen
        while l < len(left) and r < len(right):
            # fügt den kleineren der beiden Werte der sortierten Liste hinzu
            if left[l] <= right[r]:
                list_to_sort[i] = left[l]
                l += 1
            else:
                list_to_sort[i] = right[r]
                r += 1
            i += 1
        

        # An diesem Punkt ist nur eine der Listen "left" und "right" nicht leer.
        # Daher fügen wir den Rest dieser Liste an die gemeinsame Liste an.
        if l < len(left):
            list_to_sort[i:] = left[l:]
            
        if r < len(right):
            list_to_sort[i:] = right[r:]
            
            
import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
merge_sort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
