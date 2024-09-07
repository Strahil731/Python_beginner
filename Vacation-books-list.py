all_page_current_book = int(input())
read_page_per_one_hour = int(input())
days_need_read_book = int(input())

need_time_to_read_book = int(all_page_current_book / read_page_per_one_hour)
need_hours_per_day = int(need_time_to_read_book / days_need_read_book)

print(need_hours_per_day)