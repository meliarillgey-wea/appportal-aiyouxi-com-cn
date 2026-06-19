SITE_SUMMARY = {
    "name": "爱游戏门户",
    "url": "https://appportal-aiyouxi.com.cn",
    "keywords": ["爱游戏", "游戏资讯", "手游推荐", "游戏评测"],
    "tags": ["游戏", "门户", "手游", "社区"],
    "description": "爱游戏是一个专注手游推荐与评测的综合性游戏门户，提供最新游戏资讯、热门游戏排行及玩家社区互动功能。",
    "category": "游戏资讯",
    "language": "zh-CN",
    "last_updated": "2025-02-01"
}

def extract_summary(data: dict) -> dict:
    """从站点资料字典中提取结构化摘要信息。"""
    return {
        "标题": data.get("name", ""),
        "网址": data.get("url", ""),
        "核心关键词": ", ".join(data.get("keywords", [])),
        "标签": ", ".join(data.get("tags", [])),
        "简介": data.get("description", ""),
        "分类": data.get("category", ""),
        "语言": data.get("language", ""),
        "最近更新": data.get("last_updated", ""),
    }

def format_summary_block(summary: dict) -> str:
    """将摘要字典格式化为易读的多行字符串。"""
    lines = []
    lines.append("=" * 50)
    lines.append("        站点结构化摘要")
    lines.append("=" * 50)
    for key, value in summary.items():
        lines.append(f"{key:10s} : {value}")
    lines.append("=" * 50)
    return "\n".join(lines)

def validate_summary(summary: dict) -> bool:
    """检查摘要是否包含必要的字段。"""
    required = ["标题", "网址", "核心关键词", "简介"]
    for field in required:
        if field not in summary or not summary[field]:
            return False
    return True

def build_report(data: dict) -> str:
    """组合提取、验证、格式化，生成最终报告。"""
    summary = extract_summary(data)
    if not validate_summary(summary):
        return "[错误] 摘要数据不完整，无法生成报告。"
    return format_summary_block(summary)

def main():
    report = build_report(SITE_SUMMARY)
    print(report)

if __name__ == "__main__":
    main()