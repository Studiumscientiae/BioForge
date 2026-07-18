"""
Central UI theme configuration for BioForge.
"""

# ==========================================================
# Typography
# ==========================================================

TITLE_FONT_SIZE = 24
SUBTITLE_FONT_SIZE = 12
FOOTER_FONT_SIZE = 12

SECTION_TITLE_FONT = ("Arial", 16, "bold")
RESULT_TITLE_FONT = ("Arial", 20, "bold")


# ==========================================================
# Widget Styles
# ==========================================================

# Frames

FRAME_CORNER_RADIUS = 10

# Buttons

BUTTON_WIDTH = 140
BUTTON_HEIGHT = 36
BUTTON_CORNER_RADIUS = 8

# Entries

ENTRY_HEIGHT = 36

# Comboboxes

COMBOBOX_HEIGHT = 36

# Textboxes

TEXTBOX_HEIGHT = 250


# ==========================================================
# Common Spacing
# ==========================================================

SPACE_XS = 2
SPACE_SM = 5
SPACE_MD = 10
SPACE_LG = 15
SPACE_XL = 20


# ==========================================================
# Sidebar
# ==========================================================

SIDEBAR_WIDTH = 220
SIDEBAR_CORNER_RADIUS = 12

# Navigation Buttons

NAV_BUTTON_HEIGHT = 40
NAV_BUTTON_CORNER_RADIUS = 8
NAV_BUTTON_PADDING_Y = SPACE_SM

ACTIVE_BUTTON_COLOR = ("gray70", "gray30")
INACTIVE_BUTTON_COLOR = ("gray25", "gray25")

# Sidebar Layout

LOGO_PADDING_X = SPACE_LG
LOGO_PADDING_Y = (SPACE_XL, SPACE_MD)

NAVIGATION_PADDING_X = SPACE_MD
NAVIGATION_PADDING_Y = SPACE_MD

FOOTER_PADDING_X = SPACE_LG
FOOTER_PADDING_Y = (SPACE_MD, SPACE_XL)


# ==========================================================
# Analysis Page & Validation Page
# ==========================================================

# Layout

LEFT_PANEL_PADX = (SPACE_MD, SPACE_SM)
LEFT_PANEL_PADY = SPACE_MD

RIGHT_PANEL_PADX = (SPACE_SM, SPACE_MD)
RIGHT_PANEL_PADY = SPACE_MD

# Section Frames

FRAME_PADX = SPACE_LG
FRAME_PADY = SPACE_MD
FRAME_TOP_PADY = (SPACE_LG, SPACE_MD)

# Section Titles

SECTION_TITLE_PADX = SPACE_MD
SECTION_TITLE_PADY = (SPACE_MD, SPACE_SM)

# Checkboxes

CHECKBOX_PADX = SPACE_LG
CHECKBOX_PADY = SPACE_XS
CHECKBOX_PADY_END = (SPACE_XS, SPACE_MD)

# Action Buttons

ACTION_BUTTON_PADX = SPACE_LG
ACTION_BUTTON_PADY = (SPACE_LG, SPACE_LG)

# Result Panel

RESULT_TITLE_PADX = SPACE_LG
RESULT_TITLE_PADY = (SPACE_LG, SPACE_MD)

RESULT_PANEL_PADX = SPACE_LG
RESULT_PANEL_PADY = SPACE_MD
TEXTBOX_FONT = ("Consolas", 13)

# Labels

LABEL_PADX = SPACE_LG

# Entries

ENTRY_PADX = SPACE_LG
ENTRY_PADY = (SPACE_SM, SPACE_LG)

# Comboboxes

COMBOBOX_PADX = SPACE_LG
COMBOBOX_PADY = (SPACE_SM, SPACE_XL)

# Textboxes

TEXTBOX_PADX = SPACE_LG
TEXTBOX_PADY = (SPACE_SM, SPACE_LG)

# Buttons

BUTTON_PADY = SPACE_SM
BUTTON_PADY_END = (SPACE_SM, SPACE_XL)