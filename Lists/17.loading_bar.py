def loading_bar_percent(percent_loaded):
    if percent_loaded == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    percent = percent_loaded // 10
    dots = 10 - percent
    return f"{percent_loaded}% [{'%' * percent}{'.' * dots}]\nStill loading..."

percent_of_bar = int(input())
print(loading_bar_percent(percent_of_bar))