def oxford_comma(list):
    if len(list) == 1:
        return list[0]
    elif len(list) == 2:
        return ' and '.join(list)
    elif len(list) >= 3:
      list[-1] = 'and ' + list[-1]
      print(list)
      return ', '.join(list)
print(oxford_comma(['kiwi', 'banana', 'hel']))