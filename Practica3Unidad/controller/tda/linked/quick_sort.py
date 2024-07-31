
class QuickSort:
    
    @staticmethod
    def quick_sort_attribute_ascendent(array, attribute):
        if len(array) <= 1:
            return array
        else:
            pivot = array[len(array) // 2]
            less = [x for x in array if getattr(x, attribute) < getattr(pivot, attribute)]
            equal = [x for x in array if getattr(x, attribute) == getattr(pivot, attribute)]
            greater = [x for x in array if getattr(x, attribute) > getattr(pivot, attribute)]
            return QuickSort.quick_sort_attribute_ascendent(less, attribute) + equal + QuickSort.quick_sort_attribute_ascendent(greater, attribute)
    
    @staticmethod
    def quick_sort_attribute_descendent(array, attribute):
        if len(array) <= 1:
            return array
        else:
            pivot = array[len(array) // 2]
            less = [x for x in array if getattr(x, attribute) > getattr(pivot, attribute)]
            equal = [x for x in array if getattr(x, attribute) == getattr(pivot, attribute)]
            greater = [x for x in array if getattr(x, attribute) < getattr(pivot, attribute)]
            return QuickSort.quick_sort_attribute_descendent(less, attribute) + equal + QuickSort.quick_sort_attribute_descendent(greater, attribute)
