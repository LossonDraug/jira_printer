# This is a sample Python script.
import csv
import jinja2

from card import Cards

STORY_TEMPLATE_FILE = "card_template.html.j2"
FEATURE_TEMPLATE_FILE = "feature_template.html.j2"


def read_cards(file_name: str):
    with open(file_name, encoding='utf-8', errors='ignore') as jira_export_file:
        jira_export_csv = csv.reader(jira_export_file)
        cards = Cards(next(jira_export_csv))
        for row in jira_export_csv:
            cards.add_card(row)
    return cards


def render_cards(cards: list, template: str, name: str):
    template_loader = jinja2.FileSystemLoader(searchpath="templates/")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(template)
    output = template.render(cards=cards)
    with open("output/" + name + ".html", "w") as f:
        f.write(output)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cards = read_cards("input/tasks_full.csv")
    render_cards(cards.story_cards, STORY_TEMPLATE_FILE, "stories")
    render_cards(cards.feature_cards, FEATURE_TEMPLATE_FILE, "epics")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
