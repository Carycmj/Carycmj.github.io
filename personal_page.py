#!/usr/bin/env python3
"""Generate a static personal homepage for GitHub Pages.

Usage:
    python personal_page.py
"""

from __future__ import annotations

from html import escape
from pathlib import Path


PROFILE = {
    "name": "曹梦杰",
    "title": "大模型评测运营 / 产品运营",
    "location": "上海",
    "email": "Carycmj@outlook.com",
    "github": "https://github.com/Carycmj",
    "linkedin": "",
    "bio": (
        "北京交通大学企业管理硕士在读（2023.09-2026.06）。"
        "专注大模型评测与应用评测、数据体系建设与产品运营。"
    ),
    "skills": [
        "大模型评测",
        "数据集建设",
        "指标体系设计",
        "数据分析",
        "Python / SQL",
        "A/B测试",
        "AI工具使用",
    ],
}

AWARDS = [
    "“正大杯”第十五届市场调查与分析大赛北京赛区（研究生组）一等奖（2025.01-2025.04）",
    "2024年“挑战杯”首都大学生创业计划竞赛北京市三等奖（2024.04-2024.05）",
    "第二届全国大学生数据统计与分析竞赛二等奖（2023.06）",
]

PROJECTS = [
    {
        "name": "美团 | 大模型评测运营",
        "description": "构建开放问题评测框架、数据集与打分方案；推动应用评测类目体系与数据集建设。",
        "link": "https://github.com/Carycmj/Carycmj.github.io",
    },
    {
        "name": "理想 | 绩效AI产品",
        "description": "搭建数据处理Pipeline与自动化分析；支持AI Talent能力评估与业务决策。",
        "link": "https://github.com/Carycmj/Carycmj.github.io",
    },
    {
        "name": "京东 | 数据运营",
        "description": "搭建招聘数据口径与指标体系，推进数据自动化更新与流程优化。",
        "link": "https://carycmj.github.io",
    },
]


def _render_skill_badges(skills: list[str]) -> str:
    return "\n".join(f'<span class="badge">{escape(skill)}</span>' for skill in skills)


def _render_projects(projects: list[dict[str, str]]) -> str:
    cards = []
    for project in projects:
        name = escape(project["name"])
        desc = escape(project["description"])
        link = escape(project["link"])
        cards.append(
            f"""
            <article class="card">
              <h3>{name}</h3>
              <p>{desc}</p>
              <a href="{link}" target="_blank" rel="noreferrer">View on GitHub</a>
            </article>
            """.strip()
        )
    return "\n".join(cards)


def _render_awards(awards: list[str]) -> str:
    return "\n".join(f"<li>{escape(item)}</li>" for item in awards)


def render_html(profile: dict[str, str | list[str]], projects: list[dict[str, str]]) -> str:
    name = escape(str(profile["name"]))
    title = escape(str(profile["title"]))
    location = escape(str(profile["location"]))
    email = escape(str(profile["email"]))
    github = escape(str(profile["github"]))
    linkedin = escape(str(profile["linkedin"]))
    bio = escape(str(profile["bio"]))
    skills_html = _render_skill_badges(list(profile["skills"]))  # type: ignore[arg-type]
    projects_html = _render_projects(projects)
    awards_html = _render_awards(AWARDS)

    linkedin_link = ""
    if profile.get("linkedin"):
        linkedin_link = f'<a href="{linkedin}" target="_blank" rel="noreferrer">LinkedIn</a>'

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{name} | Personal Homepage</title>
  <style>
    :root {{
      --bg: #f6f8ff;
      --panel: #ffffff;
      --text: #1b1f2a;
      --subtle: #5d6475;
      --brand: #104f8c;
      --accent: #d7ecff;
      --line: #dbe2ef;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: "Avenir Next", "Segoe UI", sans-serif;
      color: var(--text);
      background:
        radial-gradient(circle at 10% 0%, #e7f1ff 0%, transparent 38%),
        radial-gradient(circle at 90% 20%, #eaf6ec 0%, transparent 34%),
        var(--bg);
      line-height: 1.6;
    }}
    .container {{
      max-width: 920px;
      margin: 0 auto;
      padding: 56px 20px 72px;
    }}
    .hero {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 20px;
      padding: 28px;
      box-shadow: 0 10px 30px rgba(16, 79, 140, 0.08);
    }}
    h1 {{
      font-size: 2rem;
      margin-bottom: 6px;
    }}
    .title {{
      color: var(--brand);
      font-weight: 700;
      margin-bottom: 6px;
    }}
    .location {{
      color: var(--subtle);
      margin-bottom: 16px;
    }}
    .bio {{
      margin-bottom: 18px;
      max-width: 70ch;
    }}
    .links {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .links a {{
      border: 1px solid var(--line);
      background: #fff;
      color: var(--text);
      text-decoration: none;
      padding: 8px 12px;
      border-radius: 999px;
      font-size: 0.95rem;
      transition: all 0.18s ease;
    }}
    .links a:hover {{
      border-color: var(--brand);
      color: var(--brand);
      transform: translateY(-1px);
    }}
    section {{
      margin-top: 22px;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 20px;
      padding: 24px;
    }}
    section h2 {{
      font-size: 1.2rem;
      margin-bottom: 14px;
    }}
    .badges {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .badge {{
      background: var(--accent);
      color: #0f3359;
      padding: 6px 12px;
      border-radius: 999px;
      font-size: 0.9rem;
      border: 1px solid #c6def8;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 14px;
    }}
    .card {{
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 16px;
      background: #fff;
    }}
    .card h3 {{
      font-size: 1rem;
      margin-bottom: 8px;
    }}
    .card p {{
      color: var(--subtle);
      margin-bottom: 10px;
      min-height: 3.2em;
    }}
    .card a {{
      color: var(--brand);
      text-decoration: none;
      font-weight: 600;
    }}
    .card a:hover {{
      text-decoration: underline;
    }}
    .list {{
      padding-left: 18px;
      color: var(--subtle);
    }}
    .list li {{
      margin-bottom: 8px;
    }}
    footer {{
      margin-top: 16px;
      color: var(--subtle);
      font-size: 0.9rem;
      text-align: center;
    }}
    @media (max-width: 740px) {{
      .container {{
        padding-top: 26px;
      }}
      h1 {{
        font-size: 1.6rem;
      }}
      .grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>
  <main class="container">
    <header class="hero">
      <h1>{name}</h1>
      <p class="title">{title}</p>
      <p class="location">{location}</p>
      <p class="bio">{bio}</p>
      <div class="links">
        <a href="mailto:{email}">Email</a>
        <a href="{github}" target="_blank" rel="noreferrer">GitHub</a>
        {linkedin_link}
      </div>
    </header>

    <section>
      <h2>Skills</h2>
      <div class="badges">
        {skills_html}
      </div>
    </section>

    <section>
      <h2>Awards</h2>
      <ul class="list">
        {awards_html}
      </ul>
    </section>

    <section>
      <h2>Projects</h2>
      <div class="grid">
        {projects_html}
      </div>
    </section>

    <footer>Built with Python + GitHub Pages</footer>
  </main>
</body>
</html>
"""


def main() -> None:
    here = Path(__file__).resolve().parent
    output = here / "index.html"
    output.write_text(render_html(PROFILE, PROJECTS), encoding="utf-8")

    print(f"Generated: {output}")
    print("\nNext steps:")
    print("1) Edit PROFILE and PROJECTS in personal_page.py")
    print("2) Re-run: python personal_page.py")
    print("3) Push index.html to a GitHub repo")
    print("4) In GitHub repo: Settings -> Pages -> Deploy from branch")
    print("5) Select branch 'main' and folder '/ (root)'")


if __name__ == "__main__":
    main()
