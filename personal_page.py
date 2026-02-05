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
    "phone": "(86) 177-6622-0062",
    "email": "Carycmj@outlook.com",
    "location": "上海",
    "title": "产品运营",
}

EDUCATION = [
    {
        "school": "北京交通大学",
        "degree": "企业管理 硕士",
        "time": "2023.09 - 2026.06",
        "details": "核心课程：数据挖掘与商务智能、中级计量经济学、组织行为理论、战略管理等",
    },
    {
        "school": "苏州大学",
        "degree": "管理学（辅修心理学） 本科",
        "time": "2019.09 - 2023.06",
        "details": (
            "GPA: 3.8/4.0（前10%）；核心课程：高等数学、线性代数、运筹学、统计学、"
            "微观经济学、宏观经济学等；荣誉：优秀毕业生、三好学生、学习优秀奖学金、"
            "精神文明奖学金等"
        ),
    },
]

EXPERIENCE = [
    {
        "org": "美团",
        "role": "M17 大模型评测团队 评测运营",
        "time": "2025.04 - 至今",
        "location": "北京",
        "sections": [
            {
                "title": "开放问题评测",
                "bullets": [
                    "评测框架：「背景目标」针对传统主观评测中个人偏好噪声大、稳定性低的行业痛点，旨在构建一套剥离个人偏好、基于群体共识的自动化评测体系；「行动&结果」聚焦指令遵循、安全性、真实性等高共识维度，将评价标准拆解为细粒度的原子化指标，设计并落地“准入判定-基准定档-缺陷降档”的三级分层聚合框架，替代传统模糊打分逻辑，最终产出高置信度的绝对分指标及模型对战榜单。",
                    "数据建设：「背景目标」为支撑评测框架，需构建一个覆盖真实分布、高难度且易达成共识的基准数据集；「行动&结果」基于C端/B端头部高频需求，采用“高质量种子+场景化扩写”的作业模式，构建了覆盖中英文、多任务的2000+条高难度开放数据集；",
                    "打分方案：「背景目标」为高效指导文本模型的快速、精准迭代，期望有一个对齐人类偏好、打分稳定的评估模型；「行动&结果」采用“ModelEval初评 + Human-in-the-loop质检”的混合评估模式，自动化评估准确率超70%；产出的模型对战榜单与LMSYS Chatbot Arena的PLCC达到0.7+，成功支持LongCat系列模型的多轮迭代上线；",
                ],
            },
            {
                "title": "应用评测",
                "bullets": [
                    "类目体系建设：「背景目标」面对高复杂度的C/B端需求，期望快速寻找高价值场景，指导评测开展；「行动&结果」基于内外部调研，构建“行业/场景/任务”三级类目体系，定义代码、商品零售、金融等10大行业，并进行二级场景细分；同时参考Anthropic Economic Index百万数据聚类后的600+任务构建规划、创作、数据分析等8大任务；该体系成功指导了应用评测集V2.0/V2.1的数据分布均衡化。",
                    "主客观数据集建设：「背景目标」针对早期评测集建设流程模糊、人工依赖度高的问题，期望通过SOP优化提升数据生产的透明度与数据质量；「行动&结果」基于类目体系开展数据分布对齐，制定高区分度与真实性标准；重构数据建设SOP，覆盖“挖掘-打标-质检-校验”全链路，并引入LLM-as-a-Judge实现自动化预标注与分流质检，显著提升数据生产人效；最终交付应用评测集V2.0，定向补充150+条复杂工具调用（Function Call）客观题与200+条垂类行业主观题。",
                ],
            },
        ],
    },
    {
        "org": "理想",
        "role": "COE（专家中心） 绩效AI产品",
        "time": "2024.11 - 2025.02",
        "location": "北京",
        "sections": [
            {
                "title": "数据自动化",
                "bullets": [
                    "「背景目标」针对绩效分析场景中数据源分散、重复劳动多的痛点，旨在重构数据处理流程，实现从清洗到可视化的全链路自动化分析，释放人力资源；「行动&结果」基于Python构建端到端的数据处理Pipeline，打通飞书绩效与本地数据流，自动化完成清洗、50+核心指标逻辑运算及多维交叉验证，实现图表绘制与PPT报告的一键输出；将季度/年度分析周期由5天压缩至1天，显著降低人工操作误差。",
                ],
            },
            {
                "title": "销售AI Talent",
                "bullets": [
                    "「背景目标」解决销售人才画像模糊、成长路径难以量化的痛点，期望构建数据驱动的金牌专家识别体系与能力评估模型，推动人才全生命周期管理的闭环落地；「行动&结果」处理千万级业务流水值数据，并引入LLM对非结构化文本数据进行语义打标，构建覆盖销售专家“过往履历/基础素质/业务绩效”的全生命周期200+高维特征库；利用统计、聚类构建专家画像，基于随机森林、XGBoost等训练金牌专家预测模型，正确率（ACC）达80%+，同时引入SHAP值进行模型可解释性分析，输出关键影响因子以指导业务管理；基于低代码平台在3个月内完成从算法原型到销售AI Talent前端产品的搭建与测试，实现了从模型预测到业务决策辅助的闭环交付；",
                ],
            },
        ],
    },
    {
        "org": "京东",
        "role": "COE（专家中心） 数据运营",
        "time": "2024.05 - 2024.08",
        "location": "北京",
        "sections": [
            {
                "title": "数据运营",
                "bullets": [
                    "「背景目标」子集团招聘需求大、人力有限，需快速利用数据帮助招聘团队提效，但数据繁杂、口径不一；期望快速搭建招聘数据中台，助力团队优化招聘流程。「行动&结果」梳理招聘全流程数据，撰写指标说明书（含招聘结果、效率、进度、质量、合规与体验五方面指标），统一计算口径，拉齐各方对数据的认知；同时，利用内部招聘看板系统、PS系统及Excel等搭建数据看板，实现周度、月度、季度的数据自动化更新，帮助招聘团队阶段性复盘与优化；此外，By多级业务部、招聘人员、岗位以及时间等维度进行深入分析，挖掘各指标卡点并优化，最终助力招聘团队达成Q3核心业务指标。",
                ],
            },
            {
                "title": "资源管控与横向项目",
                "bullets": [
                    "资源管控：招聘财务资源管控与预算，如招聘网络渠道费、差旅费、背调费、猎头费、校招费等；招聘信息资源支持，包括二次回流、绩效查询、简历信息修改等；招聘网络渠道资源支持，包括猎聘、BOSS、脉脉等的账号开通与分配。",
                    "横向项目：内部招聘看板系统4.0试点落地、内推渠道建设、面评流程规范、候选人面试体验优化、入职人员背景分析等。",
                ],
            },
        ],
    },
]

AWARDS = [
    "“正大杯”第十五届市场调查与分析大赛北京赛区（研究生组）一等奖（2025.01 - 2025.04）",
    "2024年“挑战杯”首都大学生创业计划竞赛北京市三等奖（2024.04 - 2024.05）",
    "第二届全国大学生数据统计与分析竞赛二等奖（2023.06）",
]

SKILLS = [
    "Python",
    "Js",
    "Sql",
    "Chatbot",
    "Cursor等AI工具",
    "MS Office国家二级",
    "英语（CET-6）",
]


def _render_skill_badges(skills: list[str]) -> str:
    return "\n".join(f'<span class="badge">{escape(skill)}</span>' for skill in skills)


def _render_list(items: list[str]) -> str:
    return "\n".join(f"<li>{escape(item)}</li>" for item in items)


def _render_education(items: list[dict[str, str]]) -> str:
    blocks = []
    for item in items:
        school = escape(item["school"])
        degree = escape(item["degree"])
        time = escape(item["time"])
        details = escape(item["details"])
        blocks.append(
            f"""
            <article class="edu">
              <div class="row">
                <h3>{school}</h3>
                <span class="muted">{time}</span>
              </div>
              <p class="muted">{degree}</p>
              <p>{details}</p>
            </article>
            """.strip()
        )
    return "\n".join(blocks)


def _render_experience(items: list[dict[str, object]]) -> str:
    blocks = []
    for item in items:
        org = escape(str(item["org"]))
        role = escape(str(item["role"]))
        time = escape(str(item["time"]))
        location = escape(str(item["location"]))
        sections = item["sections"]
        section_html = []
        for section in sections:  # type: ignore[assignment]
            title = escape(str(section["title"]))
            bullets = _render_list(list(section["bullets"]))  # type: ignore[arg-type]
            section_html.append(
                f"""
                <div class="exp-section">
                  <h4>{title}</h4>
                  <ul class="list">
                    {bullets}
                  </ul>
                </div>
                """.strip()
            )
        blocks.append(
            f"""
            <article class="exp">
              <div class="row">
                <h3>{org}</h3>
                <span class="muted">{time}</span>
              </div>
              <div class="row">
                <p class="muted">{role}</p>
                <span class="muted">{location}</span>
              </div>
              {''.join(section_html)}
            </article>
            """.strip()
        )
    return "\n".join(blocks)


def render_html(profile: dict[str, str | list[str]]) -> str:
    name = escape(str(profile["name"]))
    title = escape(str(profile["title"]))
    location = escape(str(profile["location"]))
    email = escape(str(profile["email"]))
    phone = escape(str(profile["phone"]))
    education_html = _render_education(EDUCATION)
    experience_html = _render_experience(EXPERIENCE)
    awards_html = _render_list(AWARDS)
    skills_html = _render_list(SKILLS)

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
    .links .pill {{
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
    .avatar {{
      width: 120px;
      height: 120px;
      border-radius: 16px;
      object-fit: cover;
      border: 1px solid var(--line);
      background: #f0f3f9;
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
    .row {{
      display: flex;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
      align-items: baseline;
    }}
    .muted {{
      color: var(--subtle);
    }}
    .edu, .exp {{
      padding: 12px 0;
      border-top: 1px solid var(--line);
    }}
    .edu:first-child, .exp:first-child {{
      border-top: none;
      padding-top: 0;
    }}
    .exp-section {{
      margin-top: 10px;
    }}
    .exp-section h4 {{
      font-size: 1rem;
      margin-bottom: 6px;
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
      <div>
        <h1>{name}</h1>
        <p class="title">{title}</p>
        <p class="location">{location}</p>
        <div class="links">
          <span class="pill">{phone}</span>
          <span class="pill">{email}</span>
          <span class="pill">{location}</span>
        </div>
      </div>
    </header>

    <section>
      <h2>学历背景</h2>
      {education_html}
    </section>

    <section>
      <h2>实习经历</h2>
      {experience_html}
    </section>

    <section>
      <h2>竞赛活动</h2>
      <ul class="list">
        {awards_html}
      </ul>
    </section>

    <section>
      <h2>个人技能</h2>
      <ul class="list">
        {skills_html}
      </ul>
    </section>

    <footer>Built with Python + GitHub Pages</footer>
  </main>
</body>
</html>
"""


def main() -> None:
    here = Path(__file__).resolve().parent
    output = here / "index.html"
    output.write_text(render_html(PROFILE), encoding="utf-8")

    print(f"Generated: {output}")
    print("\nNext steps:")
    print("1) Edit PROFILE and PROJECTS in personal_page.py")
    print("2) Re-run: python personal_page.py")
    print("3) Push index.html to a GitHub repo")
    print("4) In GitHub repo: Settings -> Pages -> Deploy from branch")
    print("5) Select branch 'main' and folder '/ (root)'")


if __name__ == "__main__":
    main()
