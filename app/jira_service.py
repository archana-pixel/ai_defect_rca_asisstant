import os
import logging
import re
from jira import JIRA

class JiraService:

    def __init__(self):
        self.client = JIRA(
            server=os.getenv("JIRA_URL"),
            basic_auth=(
                os.getenv("JIRA_USERNAME"),
                os.getenv("JIRA_API_TOKEN")
            )
        )
        logging.info("Connected to Jira")

    def add_comment(self, issue_key, comment_text):
        self.client.add_comment(issue_key, comment_text)

    def add_label(self, issue_key, label):
        issue = self.client.issue(issue_key)
        labels = issue.fields.labels
        if label not in labels:
            labels.append(label)
            issue.update(fields={"labels": labels})

    def update_5why_fields(self, issue_key, rca_text):

        def extract(field):
            match = re.search(field + r":(.*?)(?=\n[A-Z]|\Z)", rca_text, re.S)
            return match.group(1).strip() if match else ""

        root_cause = extract("Root Cause")
        why1 = extract("Why1")
        why2 = extract("Why2")
        why3 = extract("Why3")
        why4 = extract("Why4")
        why5 = extract("Why5")

        issue = self.client.issue(issue_key)

        issue.update(fields={
            "customfield_10123": root_cause,
            "customfield_10124": why1,
            "customfield_10125": why2,
            "customfield_10126": why3,
            "customfield_10127": why4,
            "customfield_10128": why5,
        })

        logging.info("5-Why fields updated")