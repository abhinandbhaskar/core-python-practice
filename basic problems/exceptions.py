# try:
#     statements that may cause Exceptions
# except Exception1:
#     statements to hadle Exception1
# except Exception2:
#     statements to hadle Exception2
# else:
#     statements executed when there are no Exceptions
# finally:
#     statements executed always

# try:
#     for i in range(5):
#         print(i/0)
# except Exception as e:
#     print("Error Occured",e)
# else:
#     print("There is no Problems")
# finally:
#     print("Task Completed")

try:
    list1=[1,2,3]
    print(list1[10])
except ZeroDivisionError:
    print("Divided By Zero Error")
except OverflowError:
    print("Overflow Error Occured")
except IndexError:
    print("Index Error Occured")
except RuntimeError:
    print("Runtime Error Occured")
else:
    print("No Issues")
finally:
    print("Completed")