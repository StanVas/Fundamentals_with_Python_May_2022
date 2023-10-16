loading_bar_status = int(input())


def loading_bar_progress(bar_current_value):
    if bar_current_value == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    return f"{loading_bar_status}% [{'%' * (loading_bar_status//10)}{'.'*(10-loading_bar_status//10)}]\nStill loading..."


print(loading_bar_progress(loading_bar_status))
