*** Settings ***

Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/selenium.robot
Resource  Selenium2Screenshots/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote


*** Variables ***

@{DIMENSIONS}  1024  800
${RESOURCE_DIR}  ${CURDIR}

${BROWSER} =  chrome
${SELECTOR_CONTENTMENU_DISPLAY_LINK}  css=#plone-contentmenu-display a
${SELECTOR_CONTENTMENU_DISPLAY_ITEMS}  css=#plone-contentmenu-display ul

${SELECTOR_TOOLBAR}  css=#edit-zone



*** Keywords ***

a logged-in site administrator
  Enable autologin as  Site Administrator  Contributor  Reviewer

an example document
  Create content  type=Document
  ...  id=example-document
  ...  title=Example Document
  ...  description=This is an example document
  ...  text=<p>This document ist for testing only!</p>
  ...  container=/plone


Setup Example Content
    Open test browser

    Given a logged-in site administrator
      and an example document
    Run keyword and ignore error  Set window size  1280  1024
