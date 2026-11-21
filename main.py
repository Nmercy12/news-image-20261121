import hashlib
import os

from PIL import Image, ImageDraw, ImageFont


CREAM = (252, 249, 239)
INK = (22, 20, 18)
RED = (164, 22, 26)
BRIGHT_RED = (198, 32, 36)
GREY = (92, 88, 82)
LIGHT_GREY = (214, 208, 196)
PALE_BLUE = (222, 234, 238)
TAN = (226, 210, 178)

FONT_CANDIDATES = {
    "serif-bold": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
    ],
    "serif-italic": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf",
    ],
    "sans": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ],
    "sans-bold": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ],
    "sans-italic": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf",
    ],
    "sans-condensed": [
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ],
}


def font(kind, size):
    for path in FONT_CANDIDATES[kind]:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


F_MAST = font("serif-bold", 45)
F_SUB = font("serif-italic", 17)
F_TOPBAR = font("sans-bold", 10)
F_TOPRIGHT = font("sans-bold", 9)
F_KPI_NUM = font("sans-bold", 22)
F_KPI_CAP = font("sans", 10)
F_REGION = font("sans-bold", 10)
F_SECTION = font("sans-bold", 10)
F_TIME = font("sans-bold", 10)
F_TIME_TXT = font("sans", 9)
F_KICKER = font("sans-bold", 10)
F_LEAD_HEAD = font("serif-bold", 14)
F_LEAD_BODY = font("sans", 9)
F_SOURCE = font("sans", 9)
F_KL = font("sans-bold", 9)
F_TAG = font("sans-bold", 8)
F_SMALL_HEAD = font("sans-bold", 9)
F_SMALL_BODY = font("sans", 8)
F_SMALL_SRC = font("sans", 9)
F_SMALL_KL = font("sans-bold", 9)
F_MAP = font("sans-bold", 9)
F_LIST = font("sans-condensed", 10)
F_FOOT = font("sans", 9)
F_CHECK = font("sans", 10)


def wrap(draw, text, fnt, max_width):
    words = text.split()
    lines = []
    line = ""
    for word in words:
        trial = word if not line else line + " " + word
        if draw.textlength(trial, font=fnt) <= max_width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def para(draw, text, fnt, x, y, max_width, fill=INK, leading=2, center=False):
    lines = wrap(draw, text, fnt, max_width)
    line_h = fnt.size + leading
    for line in lines:
        if center:
            draw.text((x + max_width / 2, y), line, font=fnt, fill=fill, anchor="ma")
        else:
            draw.text((x, y), line, font=fnt, fill=fill)
        y += line_h
    return y


def icon_cop31(d, x, y):
    d.ellipse((x, y, x + 54, y + 54), outline=INK, width=2)
    d.ellipse((x + 15, y, x + 39, y + 54), outline=INK, width=1)
    d.arc((x - 5, y + 15, x + 59, y + 39), 0, 360, fill=INK, width=1)
    d.line((x, y + 27, x + 54, y + 27), fill=INK, width=1)
    d.rounded_rectangle((x + 66, y + 6, x + 78, y + 48), radius=5, outline=INK, width=2)
    d.ellipse((x + 64, y + 39, x + 80, y + 55), fill=BRIGHT_RED)
    d.rectangle((x + 69, y + 20, x + 75, y + 43), fill=BRIGHT_RED)
    d.ellipse((x + 96, y + 8, x + 142, y + 54), outline=INK, width=2)
    d.line((x + 119, y + 31, x + 119, y + 17), fill=RED, width=2)
    d.line((x + 119, y + 31, x + 131, y + 31), fill=RED, width=2)
    d.arc((x + 90, y + 2, x + 148, y + 60), 205, 335, fill=RED, width=2)


def icon_riyadh(d, x, y):
    for bx, by, bw, bh in (
        (x, y + 36, 15, 22),
        (x + 18, y + 27, 19, 31),
        (x + 40, y + 39, 13, 19),
        (x + 56, y + 20, 22, 38),
        (x + 81, y + 33, 16, 25),
        (x + 100, y + 42, 12, 16),
        (x + 115, y + 29, 20, 29),
    ):
        d.rectangle((bx, by, bx + bw, by + bh), fill=(54, 48, 45))
    for wx in (x + 24, x + 31, x + 63, x + 71, x + 122):
        d.rectangle((wx, y + 35, wx + 3, y + 39), fill=(232, 191, 100))
    d.line((x + 8, y + 61, x + 136, y + 61), fill=INK, width=1)
    for sx, sy in ((x + 30, y + 20), (x + 70, y + 4), (x + 108, y + 14)):
        d.line((sx, sy, sx + 24, sy - 17), fill=RED, width=2)
        d.ellipse((sx + 19, sy - 23, sx + 29, sy - 13), fill=(239, 177, 48))
        d.ellipse((sx + 22, sy - 20, sx + 26, sy - 16), fill=BRIGHT_RED)


def icon_peru(d, x, y):
    points = [
        (x, y + 30), (x + 10, y + 30), (x + 14, y + 18), (x + 18, y + 42),
        (x + 23, y + 8), (x + 28, y + 50), (x + 33, y + 25), (x + 38, y + 34),
        (x + 44, y + 30), (x + 70, y + 30),
    ]
    d.line(points, fill=RED, width=2)
    for hx in (x + 84, x + 110):
        d.rectangle((hx, y + 31, hx + 21, y + 47), outline=INK, width=1)
        d.polygon(((hx - 3, y + 31), (hx + 10, y + 21), (hx + 24, y + 31)), outline=INK)
        d.rectangle((hx + 8, y + 38, hx + 13, y + 47), fill=(110, 80, 55))
    d.line((x + 78, y + 51, x + 142, y + 51), fill=INK, width=1)


def mini_icon(d, kind, x, y):
    c = INK
    if kind == "bridge":
        d.line((x, y + 13, x + 22, y + 13), fill=c, width=2)
        d.arc((x, y + 3, x + 22, y + 25), 180, 360, fill=c, width=1)
        d.line((x + 3, y + 13, x + 3, y + 21), fill=c)
        d.line((x + 19, y + 13, x + 19, y + 21), fill=c)
    elif kind == "drone":
        d.ellipse((x + 7, y + 7, x + 15, y + 13), outline=c, width=1)
        d.line((x, y + 10, x + 22, y + 10), fill=c, width=1)
        d.line((x + 3, y + 5, x + 19, y + 15), fill=c, width=1)
        d.line((x + 19, y + 5, x + 3, y + 15), fill=c, width=1)
    elif kind == "atom":
        d.ellipse((x + 8, y + 8, x + 14, y + 14), fill=RED)
        d.ellipse((x + 1, y + 5, x + 21, y + 17), outline=c, width=1)
        d.ellipse((x + 5, y + 1, x + 17, y + 21), outline=c, width=1)
    elif kind == "percent":
        d.line((x + 3, y + 18, x + 19, y + 2), fill=c, width=2)
        d.ellipse((x + 2, y + 2, x + 8, y + 8), outline=c, width=1)
        d.ellipse((x + 14, y + 12, x + 20, y + 18), outline=c, width=1)
    elif kind == "flags":
        d.rectangle((x + 1, y + 3, x + 10, y + 11), fill=RED)
        d.rectangle((x + 11, y + 3, x + 20, y + 11), fill=(245, 245, 238), outline=c)
        d.ellipse((x + 14, y + 6, x + 17, y + 9), fill=RED)
        d.line((x + 1, y + 2, x + 1, y + 21), fill=c, width=1)
        d.line((x + 11, y + 2, x + 11, y + 21), fill=c, width=1)
    elif kind == "plane":
        d.polygon(((x + 11, y), (x + 22, y + 17), (x + 11, y + 13), (x, y + 17)), fill=c)
        d.line((x + 11, y + 2, x + 11, y + 20), fill=RED, width=1)
    elif kind == "speech":
        d.rounded_rectangle((x, y + 1, x + 14, y + 11), radius=2, outline=c, width=1)
        d.rounded_rectangle((x + 8, y + 8, x + 22, y + 18), radius=2, outline=RED, width=1)
        d.polygon(((x + 4, y + 11), (x + 8, y + 11), (x + 5, y + 15)), fill=c)
        d.polygon(((x + 14, y + 18), (x + 18, y + 18), (x + 16, y + 21)), fill=RED)
    elif kind == "chart":
        d.line((x, y + 19, x + 22, y + 19), fill=c, width=1)
        d.line((x + 1, y + 19, x + 1, y + 1), fill=c, width=1)
        d.line((x + 3, y + 15, x + 8, y + 10, x + 13, y + 13, x + 21, y + 3), fill=RED, width=2)
        d.ellipse((x + 19, y + 1, x + 23, y + 5), fill=RED)
    elif kind == "car":
        d.rectangle((x + 1, y + 10, x + 22, y + 17), fill=c)
        d.polygon(((x + 5, y + 10), (x + 8, y + 5), (x + 16, y + 5), (x + 20, y + 10)), fill=RED)
        d.ellipse((x + 3, y + 14, x + 8, y + 19), fill=INK)
        d.ellipse((x + 15, y + 14, x + 20, y + 19), fill=INK)
    elif kind == "bat":
        d.line((x + 5, y + 20, x + 17, y + 2), fill=(136, 93, 51), width=3)
        d.rectangle((x + 15, y, x + 22, y + 6), fill=(226, 210, 178), outline=INK)
        d.ellipse((x + 1, y + 17, x + 8, y + 23), fill=RED)


def draw_paper_texture(d):
    for i in range(0, 1024, 8):
        shade = (250, 247, 237) if (i // 8) % 2 == 0 else (252, 249, 239)
        d.line((0, i, 1024, i), fill=shade)


def build():
    img = Image.new("RGB", (1024, 1024), CREAM)
    d = ImageDraw.Draw(img)
    draw_paper_texture(d)

    # 1. Top bar
    d.text((16, 7), "THE WORLD IN ONE DAY", font=F_TOPBAR, fill=RED)
    d.text((1008, 8), "38 STORIES · 7 REGIONS · EVERY ONE DATED SATURDAY 21 NOVEMBER 2026",
           font=F_TOPRIGHT, fill=INK, anchor="ra")
    d.line((0, 26, 1024, 26), fill=INK, width=1)

    # 2. Masthead
    d.text((512, 31), "Saturday 21 November 2026", font=F_MAST, fill=INK, anchor="ma")

    # 3. Sub-headline
    d.text((512, 86), "COP31 talks run into overtime · missiles over Riyadh · a quake shakes Peru",
           font=F_SUB, fill=INK, anchor="ma")

    # 4. KPI strip
    kpis = (
        ("Day 13", "of a COP31 summit planned to close on day 12"),
        ("5", "missiles shot down over Riyadh and Jizan"),
        ("6.7", "magnitude of the quake in Junín, Peru"),
        ("146", "people safe after a jet's emergency landing"),
        ("$58,983", "bitcoin early Saturday, down 3.9% in a day"),
        ("124*", "K L Rahul's score at tea in Wellington"),
    )
    for i, (value, caption) in enumerate(kpis):
        cx = 16 + i * 166 + 83
        d.text((cx, 108), value, font=F_KPI_NUM, fill=RED, anchor="ma")
        lines = wrap(d, caption, F_KPI_CAP, 150)
        cy = 136
        for line in lines[:3]:
            d.text((cx, cy), line, font=F_KPI_CAP, fill=INK, anchor="ma")
            cy += 11
    d.line((0, 170, 1024, 170), fill=INK, width=1)

    # 5. Region bar
    regions = (
        ("Europe 5", (37, 74, 126)),
        ("Asia 10", (16, 112, 94)),
        ("Middle East 6", (148, 91, 34)),
        ("Africa 1", (114, 62, 118)),
        ("Americas 11", (35, 104, 130)),
        ("Oceania 3", (94, 68, 39)),
        ("Global 2", (64, 61, 58)),
    )
    for i, (label, colour) in enumerate(regions):
        x0 = round(i * 1024 / 7)
        x1 = round((i + 1) * 1024 / 7)
        d.rectangle((x0, 173, x1, 192), fill=colour)
        d.text(((x0 + x1) / 2, 176), label, font=F_REGION, fill=(255, 255, 255), anchor="ma")

    # 6. UTC timeline
    d.text((16, 197), "THE DAY IN UTC", font=F_SECTION, fill=GREY)
    timeline = (
        ("00:09", "Peru quake 6.7 (USGS)"),
        ("~02:00", "Riyadh intercepts, 3 missiles down"),
        ("02:08", "Bitcoin $58,983 (CoinGecko)"),
        ("18:24", "BepiColombo thrusters fire (19:24 CET, ESA)"),
        ("Morning", "COP31 third draft due"),
    )
    for i, (when, what) in enumerate(timeline):
        tx = 112 + i * 180
        d.text((tx, 196), when, font=F_TIME, fill=RED)
        para(d, what, F_TIME_TXT, tx, 207, 174, INK, 0)
    d.line((0, 226, 1024, 226), fill=INK, width=1)

    # 7. Three lead panels
    leads = (
        (
            "COP31: OVERTIME",
            "Climate summit runs into Saturday with no deal",
            "COP31 missed its Friday close. A draft with no mention of fossil fuels split nearly 200 countries; a third text is promised.",
            "(AP, Al Jazeera)",
            "1 ANTALYA, TÜRKIYE · CLIMATE",
            icon_cop31,
        ),
        (
            "SAUDI: MISSILES",
            "Five Houthi missiles shot down over Saudi Arabia",
            "The Saudi-led coalition said three were destroyed over Riyadh before dawn and two over Jizan, a day after it bombed Hodeideh port.",
            "(Reuters, AFP)",
            "2 RIYADH · JIZAN · WAR",
            icon_riyadh,
        ),
        (
            "PERU: QUAKE 6.7",
            "Magnitude 6.7 earthquake shakes central Peru",
            "The deep quake near Carhuamayo was felt in Lima and along the coast. Peru's institute reported no deaths, damage or tsunami risk.",
            "(USGS, IGP)",
            "3 JUNÍN, PERU · EARTHQUAKE",
            icon_peru,
        ),
    )
    lead_x = (16, 352, 688)
    for i, (kicker, headline, body, source, kicker_line, icon_fn) in enumerate(leads):
        lx = lead_x[i]
        icon_fn(d, lx + 90, 234)
        d.rectangle((lx, 292, lx + 320, 312), fill=RED)
        d.text((lx + 8, 296), kicker, font=F_KICKER, fill=(255, 255, 255))
        hy = para(d, headline, F_LEAD_HEAD, lx, 318, 318, INK, 2)
        by = para(d, body, F_LEAD_BODY, lx, max(hy + 3, 360), 318, INK, 1)
        d.text((lx, min(by + 3, 412)), source, font=F_SOURCE, fill=GREY)
        d.text((lx, 430), kicker_line, font=F_KL, fill=RED)
        if i == 2:
            d.rectangle((lx + 198, 426, lx + 320, 443), outline=RED)
            d.text((lx + 202, 430), "00:09 UTC · 108 km deep", font=F_TAG, fill=INK)

    # 8. Ten small panels
    smalls = (
        ("4 KYIV · WAR", "WAR", "Zelensky: Crimea bridge 'will not stay'",
         "He warns of double-tap strikes in an NBC interview.", "(NBC)", "REPORTED", "bridge", (42, 69, 122)),
        ("5 STRAIT OF HORMUZ · WAR", "WAR", "Iran says it shot down a US drone",
         "No confirmation from Washington.", "(IRIB)", "REPORTED", "drone", (141, 83, 28)),
        ("6 TEHRAN · DIPLOMACY", "DIPLOMACY", "Iran: uranium stock stays at home",
         "Minister still seeks a 'fair solution'.", "(Times of Israel)", "OFFICIAL", "atom", (118, 66, 42)),
        ("7 WASHINGTON · TECH", "TECHNOLOGY", "Trump vows tax on data centres abroad",
         "'Tremendous' penalty promised; no details yet.", "(ABC)", "REPORTED", "percent", (31, 92, 124)),
        ("8 BEIJING · DIPLOMACY", "DIPLOMACY", "China tells Japan to 'correct' Taiwan words",
         "Tokyo says its stance is unchanged.", "(Ministry, AFP)", "OFFICIAL", "flags", (24, 104, 73)),
        ("9 DAVAO · AVIATION", "AVIATION", "Jet lands safely after engine-fire alert",
         "Air Niugini 767 diverts after midnight; all 146 safe.", "(Airline, AP)", "OFFICIAL", "plane", (33, 100, 105)),
        ("10 CANBERRA · DIPLOMACY", "DIPLOMACY", "Australia and China agree to AI talks",
         "Albanese ends an 11-day trip.", "(ABC)", "OFFICIAL", "speech", (104, 64, 30)),
        ("11 WORLD · MARKETS", "MARKETS", "Bitcoin trades below $59,000 on Saturday",
         "Down 3.9% in 24 hours; ether $1,625.", "(CoinGecko, 02:08 UTC)", "CONFIRMED", "chart", (64, 61, 58)),
        ("12 LAS VEGAS · FORMULA ONE", "FORMULA ONE", "Russell fastest in final Las Vegas practice",
         "1:34.041 in a damp, messy session.", "(Formula 1)", "OFFICIAL", "car", (32, 89, 118)),
        ("13 WELLINGTON · CRICKET", "CRICKET", "Rahul hits a century against New Zealand",
         "India 344 for 2 at tea, replying to 368.", "(AFP)", "OFFICIAL", "bat", (104, 64, 30)),
    )
    for i, (label, kicker, headline, body, source, badge, icon, colour) in enumerate(smalls):
        col = i % 5
        row = i // 5
        sx = 16 + col * 200
        sy = 458 + row * 116
        d.rectangle((sx, sy, sx + 192, sy + 14), fill=colour)
        d.text((sx + 5, sy + 2), label, font=F_SMALL_KL, fill=(255, 255, 255))
        d.text((sx + 5, sy + 18), kicker, font=F_SMALL_KL, fill=RED)
        mini_icon(d, icon, sx + 166, sy + 17)
        hy = para(d, headline, F_SMALL_HEAD, sx + 4, sy + 29, 158, INK, 1)
        by = para(d, body, F_SMALL_BODY, sx + 4, max(hy + 1, sy + 52), 184, INK, 1)
        d.text((sx + 4, sy + 96), source, font=F_SMALL_SRC, fill=GREY)
        bw = 58 if badge == "CONFIRMED" else (46 if badge == "OFFICIAL" else 44)
        d.rectangle((sx + 188 - bw, sy + 94, sx + 188, sy + 104), fill=colour)
        d.text((sx + 188 - bw / 2, sy + 95), badge, font=F_SMALL_SRC, fill=(255, 255, 255), anchor="ma")

    # 9. Map and numbered list
    d.text((16, 696), "WHERE IT HAPPENED", font=F_SECTION, fill=INK)
    map_x, map_y, map_w, map_h = 16, 714, 264, 148
    d.rectangle((map_x, map_y, map_x + map_w, map_y + map_h), fill=PALE_BLUE)
    for gx in range(map_x + 20, map_x + map_w, 40):
        d.line((gx, map_y, gx, map_y + map_h), fill=(232, 240, 242))
    for gy in range(map_y + 20, map_y + map_h, 30):
        d.line((map_x, gy, map_x + map_w, gy), fill=(232, 240, 242))
    d.ellipse((map_x + 16, map_y + 22, map_x + 83, map_y + 72), fill=TAN)
    d.ellipse((map_x + 46, map_y + 68, map_x + 81, map_y + 128), fill=TAN)
    d.ellipse((map_x + 125, map_y + 20, map_x + 171, map_y + 49), fill=TAN)
    d.ellipse((map_x + 128, map_y + 47, map_x + 176, map_y + 108), fill=TAN)
    d.ellipse((map_x + 162, map_y + 22, map_x + 245, map_y + 75), fill=TAN)
    d.ellipse((map_x + 210, map_y + 101, map_x + 254, map_y + 138), fill=TAN)
    d.ellipse((map_x + 8, map_y + 12, map_x + 30, map_y + 29), fill=TAN)
    pins = (
        (1, 165, 45), (2, 181, 82), (3, 64, 103), (4, 169, 36),
        (5, 204, 70), (6, 192, 60), (7, 48, 51), (8, 228, 51),
        (9, 241, 83), (10, 244, 122), (11, 128, 133), (12, 40, 58),
        (13, 256, 134),
    )
    for number, px, py in pins:
        cx, cy = map_x + px, map_y + py
        d.ellipse((cx - 6, cy - 6, cx + 6, cy + 6), fill=RED)
        d.text((cx, cy - 4), str(number), font=F_MAP, fill=(255, 255, 255), anchor="ma")
    d.text((16, 868), "Each number is the story with that number on this page.",
           font=F_SOURCE, fill=GREY)

    d.text((292, 696), "ALSO ON SATURDAY 21 NOVEMBER 2026 — 25 MORE STORIES",
           font=F_SECTION, fill=INK)
    more = (
        "14 Kryvyi Rih: double strike kills 2 and injures 42 (Kyiv Independent)",
        "15 Copenhagen: Russian attack plot expelled (Al Jazeera)",
        "16 Antalya: EU warns COP31 risks a \"fossil summit\" (AFP)",
        "17 Antalya: Panama threatens to block the climate text (Al Jazeera)",
        "18 Antalya: Indonesia's PLN signs 6 clean-power deals (Antara)",
        "19 Yemen: Houthis threaten Jeddah and Red Sea ports (Al Jazeera)",
        "20 Washington: Vance: Iran strikes were Trump's decision (Reuters)",
        "21 Washington: lawmaker threatens SpaceX's funding (CNN)",
        "22 Texas: execution of a man of 70 takes 63 minutes (ABC)",
        "23 Los Angeles: jury convicts man of starting Palisades fire (ABC)",
        "24 Missouri: judge approves $7.25bn Roundup settlement (AFP)",
        "25 Vancouver: Canada rests defence in youth climate trial (AFP)",
        "26 Pyongyang: Kim tours factories after no Trump meeting (AFP)",
        "27 Sejong: freight train derails, no one hurt (Korea Herald)",
        "28 Taipei: budget and cash payout passed (Taipei Times)",
        "29 Bangkok: six-point plan on arsenic in two rivers (The Nation)",
        "30 New Delhi: Pakistani minister joins SCO forum in India (Dawn)",
        "31 E India: rain alerts as Akvan's remnants move inland (ETV)",
        "32 Myanmar: rights groups urge sanctions after court ruling (AP)",
        "33 Port Louis: African rating agency talks to 15 states (Al Jazeera)",
        "34 Melbourne: Cummins keeps the Australian captaincy (ABC)",
        "35 Las Vegas: Verstappen sent to stewards after contact (Autosport)",
        "36 Gaza: Israeli strike kills 3 in Gaza City (Reuters)",
        "37 Mercury: BepiColombo reaches Mercury, thrusters fire 19:24 CET (ESA)",
        "38 Warsaw: NATO's Rutte visits after missile incursion (AP)",
    )
    for i, story in enumerate(more):
        col = i // 13
        row = i % 13
        d.text((292 + col * 360, 716 + row * 11), story, font=F_LIST, fill=INK)

    # 10. Date check footer
    d.rectangle((16, 884, 1008, 972), outline=RED, width=2)
    d.text((26, 891), "DATE CHECK", font=F_SECTION, fill=RED)
    check = (
        "Left out as Friday 20 November's news: Wall Street's fall into a correction · the Russian barrage "
        "that hit Kyiv's bridges · the missile that landed in Poland · the UK–EU deal · Cyclone Akvan's "
        "landfall · Voyager 1's light-day (18 Nov). Not confirmed when drawn, so not shown: a final COP31 "
        "text. Included this time, unlike yesterday's page: BepiColombo's Mercury orbit insertion — it "
        "happened Saturday 19:24 CET (ESA), so it belongs on Saturday's page."
    )
    para(d, check, F_CHECK, 26, 906, 968, INK, 1)

    # 11. Bottom lines
    d.text((512, 984), "Every story here happened, or was first reported, on Saturday 21 November 2026. Sources named beside each story · original drawings",
           font=F_FOOT, fill=INK, anchor="ma")
    d.text((512, 997), "HOW WE CHECKED: CONFIRMED = 2+ outlets · OFFICIAL = on the record · REPORTED = one outlet · CLAIM = one side's account",
           font=F_FOOT, fill=GREY, anchor="ma")

    return img


def main():
    img = build()
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.png")
    img.save(path, format="PNG", optimize=False, compress_level=9)
    with open(path, "rb") as handle:
        digest = hashlib.sha256(handle.read()).hexdigest()
    print(path)
    print("sha256", digest)
    print("size", os.path.getsize(path))


if __name__ == "__main__":
    main()
