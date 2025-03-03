all_calculations = ['10.0F is -12 C', '20.0F is -7 C', '30.0F is -1 C',
                                      '40.0F is 4 C', '50.0F is 10 C', '60.0F is 16 C']

newest_first = list(reversed(all_calculations))


print("==== Oldest to Newest for F ====")
for item in all_calculations:
    print(item)

print()

print("==== Most Recent First ====")
for item in newest_first:
    print(item)