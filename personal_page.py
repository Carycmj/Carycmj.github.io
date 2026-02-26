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
    "name_en": "Cary",
    "phone": "(86) 177-6622-0062",
    "email": "Carycmj@outlook.com",
    "location": "江浙沪",
    "title": "AI产品运营",
    "xiaohongshu": "Cary",
    "xiaohongshu_url": "https://www.xiaohongshu.com",  # 可替换为你的小红书主页链接
    "bio": (
        "你好，我是曹梦杰。目前在北京交通大学攻读企业管理硕士，专注于数据挖掘、商务智能与战略管理。"
        "曾在美团、理想、京东等公司实习，深耕大模型评测、数据运营与 AI 产品方向。"
        "热爱用数据驱动决策，也乐于探索 Cursor、Chatbot 等 AI 工具在业务中的落地。期待与志同道合的朋友交流。"
    ),
}

EDUCATION = [
    {
        "school": "北京交通大学",
        "logo": "bjtu.png",
        "degree": "企业管理 硕士",
        "time": "2023.09 - 2026.06",
        "details": "核心课程：数据挖掘与商务智能、中级计量经济学、组织行为理论、战略管理等",
    },
    {
        "school": "苏州大学",
        "logo": "suda.png",
        "degree": "管理学（辅修心理学） 本科",
        "time": "2019.09 - 2023.06",
        "details": (
            "GPA: 3.8/4.0（前10%）；核心课程：高等数学、线性代数、运筹学、统计学、"
            "微观经济学、宏观经济学等；荣誉：优秀毕业生、三好学生、学习优秀奖学金、"
            "精神文明奖学金等"
        ),
    },
]

# 公司 logo：默认从 favicon 服务获取。可在 EXPERIENCE 中为某条添加 "logo": "xxx.png" 使用 logos/ 目录下的本地文件
LOGO_URLS = {
    "美团": "https://www.google.com/s2/favicons?domain=meituan.com&sz=128",
    "理想": "https://www.google.com/s2/favicons?domain=lixiang.com&sz=128",
    "京东": "https://www.google.com/s2/favicons?domain=jd.com&sz=128",
}

# 学校 logo：默认从 favicon 获取。可在 EDUCATION 中为某条添加 "logo": "xxx.png" 使用 logos/ 目录下的本地文件
SCHOOL_LOGO_URLS = {
    "北京交通大学": "https://www.google.com/s2/favicons?domain=bjtu.edu.cn&sz=128",
    "苏州大学": "https://www.google.com/s2/favicons?domain=suda.edu.cn&sz=128",
}

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
    {"name": "“正大杯”第十五届市场调查与分析大赛北京赛区（研究生组）一等奖", "time": "2025.01 - 2025.04"},
    {"name": "2024年“挑战杯”首都大学生创业计划竞赛北京市三等奖", "time": "2024.04 - 2024.05"},
    {"name": "第二届全国大学生数据统计与分析竞赛二等奖", "time": "2023.06 - 2023.06"},
]

SKILLS = [
    "Python",
    "JavaScript",
    "SQL",
    "Chatbot",
    "Cursor 等 AI 工具",
    "MS Office 国家二级",
    "英语 CET-6",
]

# AI 使用习惯
AI_USAGE = {
    "intro": "日常工作中深度使用 AI 工具提效，按场景分工、各取所长：",
    "daily": "Gemini",
    "daily_desc": "日常问答、资料检索、写作润色、思路梳理的首选，多模态与长上下文能力实用。",
    "coding": "Cursor",
    "coding_desc": "写代码、调试、重构的主力工具，与 IDE 深度集成，补全与对话体验流畅。",
    "media": "Gemini、Seed",
    "media_desc": "音视频处理常用这两个模型，支持多模态理解与生成。",
}


def _render_skill_tags(skills: list[str]) -> str:
    return "\n".join(f'<span class="skill-tag">{escape(skill)}</span>' for skill in skills)


def _render_list(items: list[str]) -> str:
    return "\n".join(f"<li>{escape(item)}</li>" for item in items)


def _render_awards(items: list[dict[str, str]]) -> str:
    blocks = []
    for item in items:
        name = escape(item["name"])
        time = escape(item["time"])
        blocks.append(
            f'<article class="award">'
            f'<div class="row"><span>{name}</span><span class="muted">{time}</span></div>'
            f"</article>"
        )
    return "\n".join(blocks)


def _render_education(items: list[dict[str, str]]) -> str:
    blocks = []
    for item in items:
        school = escape(item["school"])
        degree = escape(item["degree"])
        time = escape(item["time"])
        details_raw = item["details"]
        logo = item.get("logo") or SCHOOL_LOGO_URLS.get(str(item["school"]), "")
        logo_html = ""
        if logo:
            logo_src = f'logos/{escape(logo)}' if not logo.startswith("http") else logo
            logo_html = f'<img class="school-logo" src="{escape(logo_src)}" alt="{school} logo" />'
        # 按「；」分句换行展示，带项目符号
        parts = [p.strip() for p in details_raw.split("；") if p.strip()]
        details_html = "\n".join(f"<li>{escape(p)}</li>" for p in parts)
        details_html = f"<ul class=\"list edu-list\">{details_html}</ul>" if parts else ""
        blocks.append(
            f"""
            <article class="edu">
              <div class="row edu-title-row">
                <div class="edu-school">
                  {logo_html}
                  <h3>{school}</h3>
                </div>
                <span class="muted">{time}</span>
              </div>
              <p class="muted">{degree}</p>
              <div class="edu-details">{details_html}</div>
            </article>
            """.strip()
        )
    return "\n".join(blocks)


def _render_experience(items: list[dict[str, object]]) -> str:
    blocks = []
    for i, item in enumerate(items):
        org = escape(str(item["org"]))
        role = escape(str(item["role"]))
        time = escape(str(item["time"]))
        location = escape(str(item["location"]))
        logo = item.get("logo") or LOGO_URLS.get(str(item["org"]), "")
        logo_html = ""
        if logo:
            logo_src = f'logos/{escape(logo)}' if not logo.startswith("http") else logo
            logo_html = f'<img class="org-logo" src="{escape(logo_src)}" alt="{org} logo" />'
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
        exp_id = f"exp-{i}"
        blocks.append(
            f"""
            <article class="exp collapsible" data-exp-id="{exp_id}">
              <button type="button" class="exp-header" aria-expanded="false" aria-controls="{exp_id}-body" id="{exp_id}-btn">
                <div class="exp-header-inner">
                  <div class="row exp-title-row">
                    <div class="exp-org">
                      {logo_html}
                      <h3>{org}</h3>
                    </div>
                    <span class="muted">{time}</span>
                  </div>
                  <div class="row">
                    <p class="muted">{role}</p>
                    <span class="muted">{location}</span>
                  </div>
                </div>
                <span class="toggle-icon" aria-hidden="true">▶</span>
              </button>
              <div class="exp-body" id="{exp_id}-body" hidden>
                {''.join(section_html)}
              </div>
            </article>
            """.strip()
        )
    return "\n".join(blocks)


def render_html(profile: dict[str, str | list[str]]) -> str:
    name = escape(str(profile["name"]))
    name_en = profile.get("name_en")
    name_display = f"{name} ({escape(str(name_en))})" if name_en else name
    title = escape(str(profile["title"]))
    location = escape(str(profile["location"]))
    email = escape(str(profile["email"]))
    phone = escape(str(profile["phone"]))
    xiaohongshu = str(profile.get("xiaohongshu", "")).strip()
    xiaohongshu_url = escape(str(profile.get("xiaohongshu_url", "https://www.xiaohongshu.com")))
    xiaohongshu_html = (
        f'<li><span class="icon">📕</span> <a href="{xiaohongshu_url}" target="_blank" rel="noopener">小红书 @{escape(xiaohongshu)}</a></li>'
        if xiaohongshu else ""
    )
    education_html = _render_education(EDUCATION)
    experience_html = _render_experience(EXPERIENCE)
    awards_html = _render_awards(AWARDS)
    skills_html = _render_skill_tags(SKILLS)
    bio = escape(str(profile.get("bio", "")))
    ai_intro = escape(AI_USAGE["intro"])
    ai_daily = escape(AI_USAGE["daily"])
    ai_daily_desc = escape(AI_USAGE["daily_desc"])
    ai_coding = escape(AI_USAGE["coding"])
    ai_coding_desc = escape(AI_USAGE["coding_desc"])
    ai_media = escape(AI_USAGE["media"])
    ai_media_desc = escape(AI_USAGE["media_desc"])

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{name_display} | Personal Homepage</title>
  <style>
    :root {{
      --bg: #f8fafc;
      --panel: #ffffff;
      --text: #1e293b;
      --subtle: #64748b;
      --brand: #0f766e;
      --accent: #ccfbf1;
      --line: #e2e8f0;
      --sidebar-w: 280px;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ font-size: 18px; }}
    body {{ font-family: "Times New Roman", "楷体", "KaiTi", "STKaiti", serif; font-size: 1rem; color: var(--text); background: var(--bg); line-height: 1.7; }}
    .page {{ display: flex; min-height: 100vh; max-width: 1100px; margin: 0 auto; }}
    .sidebar {{ width: var(--sidebar-w); flex-shrink: 0; padding: 40px 24px; background: var(--panel); border-right: 1px solid var(--line); position: sticky; top: 0; height: 100vh; }}
    .avatar-wrap {{ width: 140px; height: 140px; margin: 0 auto 20px; border-radius: 50%; overflow: hidden; border: 3px solid var(--line); box-shadow: 0 4px 20px rgba(15, 118, 110, 0.12); }}
    .avatar-wrap img {{ width: 100%; height: 100%; object-fit: cover; }}
    .sidebar h1 {{ font-size: 1.4rem; font-weight: 700; text-align: center; margin-bottom: 6px; color: var(--text); }}
    .sidebar .title {{ color: var(--brand); font-weight: 600; font-size: 0.95rem; text-align: center; margin-bottom: 20px; }}
    .contact-list {{ list-style: none; padding: 0; }}
    .contact-list li {{ display: flex; align-items: center; gap: 10px; padding: 8px 0; font-size: 0.9rem; color: var(--subtle); }}
    .contact-list .icon {{ width: 18px; text-align: center; font-size: 1rem; flex-shrink: 0; }}
    .contact-list a {{ color: var(--brand); text-decoration: none; }}
    .contact-list a:hover {{ text-decoration: underline; }}
    .main {{ flex: 1; padding: 40px 48px 60px; min-width: 0; }}
    .section {{ margin-bottom: 36px; }}
    .section-title {{ font-size: 1.15rem; font-weight: 600; margin-bottom: 16px; color: var(--text); display: flex; align-items: center; gap: 8px; }}
    .section-title .emoji {{ font-size: 1.2rem; }}
    .about-text {{ color: var(--subtle); font-size: 0.98rem; line-height: 1.8; }}
    .edu, .exp {{ padding: 16px 0; border-top: 1px solid var(--line); }}
    .edu:first-child, .exp:first-child {{ border-top: none; padding-top: 0; }}
    .edu-details .edu-list {{ margin-top: 4px; }}
    .edu-details .edu-list li {{ margin-bottom: 6px; color: var(--subtle); font-size: 0.92rem; }}
    .award {{ padding: 12px 0; border-top: 1px solid var(--line); }}
    .award:first-child {{ border-top: none; padding-top: 0; }}
    .exp.collapsible {{ padding: 12px 0; }}
    .exp-header {{ width: 100%; display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; text-align: left; background: none; border: none; cursor: pointer; font: inherit; color: inherit; padding: 4px 0; }}
    .exp-header:hover {{ opacity: 0.85; }}
    .exp-header-inner {{ flex: 1; min-width: 0; }}
    .toggle-icon {{ flex-shrink: 0; color: var(--brand); font-size: 0.85rem; transition: transform 0.2s; }}
    .exp-header[aria-expanded="true"] .toggle-icon {{ transform: rotate(90deg); }}
    .exp-body {{ padding-top: 12px; padding-left: 0; }}
    .row {{ display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap; align-items: baseline; }}
    .exp-org {{ display: flex; align-items: center; gap: 10px; min-width: 0; }}
    .org-logo {{ width: 32px; height: 32px; border-radius: 6px; object-fit: contain; flex-shrink: 0; background: #f1f5f9; }}
    .edu-school {{ display: flex; align-items: center; gap: 10px; min-width: 0; }}
    .school-logo {{ width: 32px; height: 32px; border-radius: 6px; object-fit: contain; flex-shrink: 0; background: #f1f5f9; }}
    .edu h3, .exp h3 {{ font-size: 1.05rem; color: var(--text); margin: 0; }}
    .muted {{ color: var(--subtle); font-size: 0.9rem; }}
    .exp-section {{ margin-top: 12px; }}
    .exp-section h4 {{ font-size: 0.95rem; font-weight: 600; margin-bottom: 8px; color: var(--text); }}
    .list {{ padding-left: 20px; color: var(--subtle); font-size: 0.92rem; }}
    .list li {{ margin-bottom: 8px; line-height: 1.65; }}
    .skills-wrap {{ display: flex; flex-wrap: wrap; gap: 10px; }}
    .skill-tag {{ background: var(--accent); color: #0d5c55; padding: 6px 14px; border-radius: 999px; font-size: 0.9rem; border: 1px solid #99f6e4; }}
    .ai-usage {{ display: flex; flex-direction: column; gap: 14px; }}
    .ai-item {{ display: flex; flex-direction: column; gap: 4px; padding: 12px 14px; background: #f8fafc; border-radius: 12px; border: 1px solid var(--line); }}
    .ai-item .ai-label {{ color: var(--brand); font-size: 0.95rem; font-weight: 600; }}
    .ai-item p {{ margin: 0; color: var(--subtle); font-size: 0.92rem; line-height: 1.6; text-align: left; }}
    footer {{ margin-top: 40px; padding-top: 24px; border-top: 1px solid var(--line); color: var(--subtle); font-size: 0.85rem; text-align: center; }}
    @media (max-width: 860px) {{
      .page {{ flex-direction: column; }}
      .sidebar {{ width: 100%; height: auto; position: static; padding: 32px 24px; border-right: none; border-bottom: 1px solid var(--line); }}
      .avatar-wrap {{ width: 120px; height: 120px; }}
      .main {{ padding: 32px 24px 48px; }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <aside class="sidebar">
      <div class="avatar-wrap">
        <img src="avatar.png" alt="{name_display}" />
      </div>
      <h1>{name_display}</h1>
      <p class="title">{title}</p>
      <ul class="contact-list">
        <li><span class="icon">📍</span> {location}</li>
        <li><span class="icon">✉️</span> <a href="mailto:{email}">{email}</a></li>
        <li><span class="icon">📱</span> {phone}</li>
        {xiaohongshu_html}
      </ul>
    </aside>
    <main class="main">
      <section class="section">
        <h2 class="section-title"><span class="emoji">✦</span> 关于我</h2>
        <p class="about-text">{bio}</p>
      </section>
      <section class="section">
        <h2 class="section-title">学历背景</h2>
        {education_html}
      </section>
      <section class="section">
        <h2 class="section-title">实习经历</h2>
        {experience_html}
      </section>
      <section class="section">
        <h2 class="section-title">竞赛活动</h2>
        <div class="awards-list">{awards_html}</div>
      </section>
      <section class="section">
        <h2 class="section-title">AI 使用</h2>
        <p class="about-text" style="margin-bottom: 14px;">{ai_intro}</p>
        <div class="ai-usage">
          <div class="ai-item">
            <span class="ai-label">日常</span>
            <p><strong style="color: var(--text);">{ai_daily}</strong> — {ai_daily_desc}</p>
          </div>
          <div class="ai-item">
            <span class="ai-label">代码</span>
            <p><strong style="color: var(--text);">{ai_coding}</strong> — {ai_coding_desc}</p>
          </div>
          <div class="ai-item">
            <span class="ai-label">音视频</span>
            <p><strong style="color: var(--text);">{ai_media}</strong> — {ai_media_desc}</p>
          </div>
        </div>
      </section>
      <section class="section">
        <h2 class="section-title">个人技能</h2>
        <div class="skills-wrap">{skills_html}</div>
      </section>
      <footer>Built with Python + GitHub Pages</footer>
    </main>
  </div>
  <script>
    document.querySelectorAll(".exp-header").forEach(function(btn) {{
      btn.addEventListener("click", function() {{
        var body = document.getElementById(this.getAttribute("aria-controls"));
        var expanded = this.getAttribute("aria-expanded") === "true";
        this.setAttribute("aria-expanded", !expanded);
        body.hidden = expanded;
      }});
    }});
  </script>
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
