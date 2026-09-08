# AI 模板短语完整禁用表

以下短语在 AI 生成文本中出现频率远高于人类写作，是 AIGC 检测器的主要识别锚点。改写时必须全部替换或删除。

## 中文禁用短语

### 开篇模板（最危险）

| 禁用短语 | 替代方案 |
|---------|---------|
| 本研究旨在 | 直接陈述或提问 |
| 本文旨在 | 直接陈述或提问 |
| 本研究基于 | 直接说数据来源 |
| 本研究以……为样本 | "数据来自……"或直接报数 |
| 本研究采用……方法 | 直接描述操作 |
| 本研究从……角度出发 | 删除，直接进入内容 |

### 过渡模板（高频）

| 禁用短语 | 替代方案 |
|---------|---------|
| 研究表明 | 直接报数据 |
| 结果表明 | 直接报数据 |
| 结果显示 | 直接报数据 |
| 此外 | "那""问题是""还有一点" |
| 然而 | "但""问题是" |
| 因此 | 删除或用因果直接表达 |
| 综上所述 | "说到底"或直接说结论 |
| 值得注意的是 | 删除 |
| 需要特别强调的是 | 删除，直接说 |
| 在……的基础上 | 重新组织句子结构 |
| 从……的角度来看 | "说到底"或删除 |
| 基于上述分析 | 删除 |
| 总的来说 | 删除 |
| 一言以蔽之 | 删除 |

### 结论模板（高频）

| 禁用短语 | 替代方案 |
|---------|---------|
| 这一结果支持了 | "假设站住了"或直接说结论 |
| 这一发现表明 | 删除，让数据说话 |
| 对……具有重要的……意义 | 简化 |
| 本研究为……提供了…… | 简化 |
| 这一体现在 | 直接说 |
| 这一结果意味着 | 直接说 |

### 学术搭配（中频）

| 禁用短语 | 替代方案 |
|---------|---------|
| 系统性地 | "大概率""往往" |
| 存在显著差异 | "差距不小" |
| 具有突出的区分作用 | "区分度最猛" |
| 呈现出较大的个体差异 | "差异已经拉开了" |
| 具有显著的独立预测作用 | "仍然管用""还在那" |
| 解释力提升了约……个百分点 | "多出来……个百分点" |
| 存在相当规模的 | "规模不小" |
| 这一发现具有重要的……意涵 | 简化 |

### 定义模板（高频）

| 禁用短语 | 替代方案 |
|---------|---------|
| ……是指…… | 用举例和对比解释 |
| ……被定义为…… | 用描述代替定义 |
| ……指的是…… | 直接描述 |

---

## 英文禁用短语

### Opening Templates

| Banned Phrase | Alternative |
|---|---|
| This study aims to | Direct statement or question |
| The present study seeks to | Direct statement |
| This research investigates | Direct statement |
| Based on the above analysis | Remove |
| From the perspective of | Remove or restructure |

### Transition Templates

| Banned Phrase | Alternative |
|---|---|
| The results indicate | State the data directly |
| The findings suggest | State the data directly |
| Furthermore / Moreover | "The thing is" / "Problem is" |
| However, it should be noted | Remove |
| It is worth noting that | Remove |
| In addition to | Remove or restructure |
| Therefore, it can be concluded | Remove, just conclude |

### Conclusion Templates

| Banned Phrase | Alternative |
|---|---|
| In conclusion | Remove or restructure |
| This result supports the hypothesis | "The hypothesis holds" |
| This finding suggests that | Remove, let data speak |
| This study provides ... implications for | Simplify |
| Taken together | "Putting these together" |

### Definition Templates

| Banned Phrase | Alternative |
|---|---|
| X is defined as | Explain through examples |
| X refers to | Describe directly |
| X can be understood as | Show, don't tell |

---

## 使用说明

1. 改写每段前，先扫描是否包含禁用短语
2. 禁用短语在段落中出现 2 个以上，该段必被 AIGC 检测器标红
3. 替代方案不是固定的——根据上下文灵活变化，避免创造新的固定模式
4. 同一篇论文中，同一个替代表达不要使用超过 2 次