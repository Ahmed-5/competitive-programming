class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0 for _ in range(n+1)]
        for b in bookings:
            i0, i1, seats = b
            arr[i0-1] += seats
            arr[i1] -= seats
            
        for i in range(1,n):
            arr[i] += arr[i-1]
            
        return arr[:n]
        