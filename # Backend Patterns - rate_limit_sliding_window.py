# Limit based on user ip address
# Allow only 5 requests in 5 seconds
# implemented using python deque instead of redis for simplicity
from collections import defaultdict, deque
from datetime import datetime, timedelta
from rest_framework import status
from rest_framework.response import Response

''' A singleton like class and it can only have one object that shares the deque and all the requests from every users 
will invoke the make_request method using this single object. Also assuming that every calls using object.make_request(request) are synchronous'''
class RateLimitMiddleWare:  
    def __init__(self, get_response):
        self.get_response = get_response
        self.user_based_request_dict = defaultdict(deque) # key will be ip address of the user

        self.max_number_of_requests = 5
        self.window_size_in_seconds = 5

    
    def make_request(self, request):
        user_key = f"ip_address:{request.headers.get('ip_address')}"
        users_deque = self.user_based_request_dict[user_key]
        current_timestamp = datetime.utcnow()
        left_window_boundary_timestamp = current_timestamp - timedelta(seconds=self.window_size_in_seconds)
        while users_deque and users_deque[0] <= left_window_boundary_timestamp:
            users_deque.popleft()
        if len(users_deque) < self.max_number_of_requests:
            users_deque.append(current_timestamp)
            return self.get_response(request)
        return Response(status=status.HTTP_429_TOO_MANY_REQUESTS)