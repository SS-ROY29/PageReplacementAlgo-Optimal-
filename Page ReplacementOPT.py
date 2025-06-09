import random

def optimal_page_replacement(pages, frame_count):
    frames = []
    page_faults = 0

    #iterates every page to add onto frames
    for i in range(len(pages)):
        page = pages[i]

        #To prevent the same page content to insert in the frame
        if page not in frames:
            if len(frames) < frame_count:
                frames.append(page)
            else:
                # Look ahead to decide which page to replace
                future = pages[i+1:]
                index_list = []

                for frame_page in frames:
                    if frame_page in future:
                        index_list.append(future.index(frame_page))
                    else:
                        # Makes it so it Will not be used again
                        index_list.append(float('inf')) 

                # Replace the page with the farthest next use
                farthest = index_list.index(max(index_list))
                frames[farthest] = page

            page_faults += 1

        print(f"Page: {page} -> Frames: {frames}")

    print(f"\nTotal Page Faults: {page_faults}")

frames = 10
pages = [random.randint(1, 9) for _ in range(frames)]
frame_count = 3

print(f"Logical Memory: {pages}")
optimal_page_replacement(pages, frame_count)
