from collections import deque

class Solution(object):
    def countStudents(self, students, sandwiches):
        students_queue = deque(students)

        rotations = 0

        while True:
            if not students_queue:
                return 0  # all students served

            student = students_queue.popleft()
            sandwich = sandwiches[0]

            if student == sandwich:
                sandwiches.pop(0)
                rotations = 0  # reset since we made progress
            else:
                students_queue.append(student)
                rotations += 1

            if rotations == len(students_queue):
                break  # full loop done, no one wants the top sandwich

        return len(students_queue)
