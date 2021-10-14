# directly go to a course page just entering the course code

import webbrowser
course = input('Enter course code: ')
print('---------Starting---------')
webbrowser.open_new(f'https://bux.bracu.ac.bd/courses/course-v1:buX+{course.upper()}+2021_Fall/about')
