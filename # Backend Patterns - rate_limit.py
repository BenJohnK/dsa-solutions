#ip - based rate limiting
import redis

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.redis_client = redis.Redis("localhost", port=6379)

        self.number_of_max_requests = 5
        self.window_period = 60
    
    def __call__(self, request):
        ip_address = request.headers.get("ip_address")

        key = f"ratelimit:{ip_address}"

        count = self.redis_client.incr(key) # save the key in redis and increment value by 1

        if count == 1:
            self.redis_client.expire(key, 60)
        
        if count > self.number_of_max_requests:
            return Response(status=429) # rate limit exceeded message response
        else:
            response = self.get_response(request)
            return response
        
