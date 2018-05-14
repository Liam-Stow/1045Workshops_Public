queOrders = []
ordersInQueue = True

def serve(queOrders):
    queOrders.pop(0)
    
def addOrder(queOrders, orderNo):
    queOrders.append(orderNo)
    
while ordersInQueue:
    orderServed = input('Order or Serve? ')
    if orderServed == 'Order':
        orderNo = int(input('Please enter the order number: '))
        addOrder(queOrders, orderNo)
    elif orderServed == 'Serve':
        if len(queOrders) > 0:
            serve(queOrders)
        else:
            print('Add an order before serving')
            continue
    else:
        print("Please only say 'Order' or 'Serve'.")
        continue
        
    print('The order list is:', queOrders)
    
    if len(queOrders) == 0:
        ordersInQueue = False
        print('The order list is empty')
        