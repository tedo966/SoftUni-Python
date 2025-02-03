from collections import deque

suggested_links = deque(int(x) for x in input().split())
featured_articles = [int(x) for x in input().split()]
target_engagement_value = int(input())

origin_sequence = []
remainder = 0
final_fed_collection = []
while suggested_links and featured_articles:
    first_el_from_s_links = suggested_links.popleft()
    last_el_from_f_articles = featured_articles.pop()

    if first_el_from_s_links == last_el_from_f_articles:
        final_fed_collection.append(0)
        continue

    if first_el_from_s_links > last_el_from_f_articles:
        remainder = first_el_from_s_links % last_el_from_f_articles
        origin_sequence.append(first_el_from_s_links)
        if not remainder == 0:
            final_fed_collection.append(remainder *-1)
            doubled_remainder = remainder * 2
            suggested_links.append(doubled_remainder)
        else:
            final_fed_collection.append(0)

    else:
        remainder = last_el_from_f_articles % first_el_from_s_links
        origin_sequence.append(last_el_from_f_articles)
        if not remainder == 0:
            final_fed_collection.append(remainder)
            doubled_remainder = remainder * 2
            featured_articles.append(doubled_remainder)
        else:
            final_fed_collection.append(0)

print(f"Final Feed: {', '.join(str(x) for x in final_fed_collection)}")
if sum(final_fed_collection) >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {sum(final_fed_collection)}")

else:
    shortfall = target_engagement_value - sum(final_fed_collection)
    print(f"Goal not achieved! Short by: {shortfall}")






