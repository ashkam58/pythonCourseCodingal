# ================================================================
# Course: AI & Coding Grandmaster Course training (Grades 9-12)
# Module 7: Introduction to Python
# Lesson 1: Introduction to Python
# After-Class Project (ACP): Daily Routine Flowchart
# File: M7L1ACP.py
# ================================================================

"""
After Class Project (ACP): Daily Routine Flowchart

Assignment Description:
- Design a daily routine flowchart using standard flowchart symbols.
- Standard flowchart symbols:
    * Oval / Terminator: Start / End
    * Rectangle / Process: Actions (e.g., Wake up, Brush teeth, Have breakfast)
    * Diamond / Decision: Conditional checks (e.g., Is it a school day? Is homework done?)
    * Parallelogram / Input-Output: Input data or display results
    * Arrows / Flowlines: Connect the sequence of operations

This Python program simulates the daily routine logic demonstrated in the flowchart.
"""

def print_flowchart_diagram():
    print("=" * 60)
    print("           DAILY ROUTINE FLOWCHART LOGIC")
    print("=" * 60)
    print("""
       ([ START: Wake up at 7:00 AM ])
                     |
                     v
             [/ Brush Teeth & Wash /]
                     |
                     v
           { Is it a School Day? }
                 /         \\
           [Yes]/           \\[No]
               v             v
       [ Pack School Bag ]   [ Weekend Leisure ]
               |             |
               v             v
       [ Attend Classes ]    [ Read / Hobby Time ]
               \\             /
                \\           /
                 v         v
             [/ Have Lunch /]
                     |
                     v
           [ Study & Homework ]
                     |
                     v
           { Is Homework Done? } <----+
                 /         \\          |
           [No] /           \\[Yes]    |
               v             v        |
      [ Continue Study ]-----+        |
                             |
                             v
                     [ Play / Exercise ]
                             |
                             v
                     [/ Have Dinner /]
                             |
                             v
             ([ END: Sleep at 10:00 PM ])
    """)
    print("=" * 60)

def simulate_daily_routine(day_type, homework_done):
    print(f"\n--- Simulating Routine for: {day_type} ---")
    print("1. [Start] Alarm rings at 7:00 AM. Time to wake up!")
    print("2. [Process] Brushing teeth and taking a refreshing shower.")
    
    if day_type.lower() == "school":
        print("3. [Decision: School Day] -> Pack school bag, wear uniform, and head to school.")
        print("4. [Process] Attend morning classes and engage in learning activities.")
    else:
        print("3. [Decision: Weekend] -> Plan weekend fun and creative projects.")
        print("4. [Process] Practice coding on Codingal and read a favorite book.")
        
    print("5. [Input/Output] Enjoy a nutritious lunch.")
    print("6. [Process] Afternoon revision and homework session.")
    
    if homework_done:
        print("7. [Decision: Homework Complete?] -> Yes! Great job!")
    else:
        print("7. [Decision: Homework Complete?] -> Not yet. Spending 30 more minutes to finish up.")
        
    print("8. [Process] Evening playtime, outdoor sports, and relaxation.")
    print("9. [Input/Output] Family dinner time.")
    print("10. [End] Wind down and go to sleep by 10:00 PM. Good night!\n")

if __name__ == "__main__":
    print_flowchart_diagram()
    # Demonstration of the algorithm
    simulate_daily_routine(day_type="School", homework_done=True)
