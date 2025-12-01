class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort()
        
        meeting_count = [0] * n
        
        # Two heaps to track room states
        free_rooms = list(range(n))  # All rooms start free
        heapq.heapify(free_rooms)
        busy_rooms = []
        
        for start, end in meetings:
            # free rooms
            while busy_rooms and busy_rooms[0][0] <= start:
                end_time, room_idx = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room_idx)
    
            if free_rooms:
                # add to busy room
                room_idx = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room_idx))
                meeting_count[room_idx] += 1
            else:
                # wait, then add to busy room
                earliest_end, room_idx = heapq.heappop(busy_rooms)
                duration = end - start
                new_end = earliest_end + duration

                heapq.heappush(busy_rooms, (new_end, room_idx))
                meeting_count[room_idx] += 1
        
        max_meetings = max(meeting_count)
        
        for i in range(len(meeting_count)):
            if meeting_count[i] == max_meetings:
                return i
    