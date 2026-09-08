---
name: "aigc-reducer"
description: "Reduces AIGC detection rate in academic papers via 12 rewriting strategies. Invoke when user needs to lower AI-generated content rate, has an AIGC report, or wants human-like academic writing."
---

# AIGC Rate Reducer for Academic Papers

Reduce AIGC detection rates in academic papers from 70%+ down to ~15% through systematic paragraph-level rewriting strategies. Based on empirical testing across 8 rounds of iterative revision that successfully reduced AIGC rate from 76% to under 10%.

## When to Invoke

- User has an AIGC detection report (e.g., Word document with red/purple highlighted paragraphs)
- User asks to "降低AIGC率" / "reduce AI detection rate"
- User has a paper with high AIGC rate and wants it rewritten
- User mentions AIGC detection, AI-generated content flags, or similar terms

## How AIGC Detectors Work (Understanding the Enemy)

AIGC detectors analyze text for statistical patterns characteristic of AI-generated content:

1. **Perplexity uniformity**: AI text has low and consistent perplexity (predictability). Human text has jagged perplexity curves.
2. **Burstiness**: Human writing varies dramatically in sentence length and complexity. AI writing is suspiciously uniform.
3. **Template phrase detection**: Certain phrases and structures appear far more frequently in AI text than human text.
4. **Logical smoothness**: AI text flows too perfectly—every sentence connects logically to the next. Human writing has jumps, tangents, and self-corrections.
5. **Parallel structure overuse**: AI loves symmetric, numbered, or bulleted parallel structures.

## Core Strategies (12 Techniques)

### Strategy 1: Sentence Length Extreme Variation

**Problem**: AI writes sentences of uniform length (15-25 chars each).
**Fix**: Deliberately create extreme length variation. Mix 3-7 char fragments with 40+ char complex sentences.

- Before: "本研究采用文本编码方法构建指标。编码过程遵循标准化流程。各维度信度满足要求。" (uniform ~15 chars)
- After: "编码怎么做？把每个学生的五个文本字段拆开。第一份'特长与兴趣爱好'用来评兴趣探索I——兴趣清不清晰、深不深、有没有持续实践、跨不跨领域。" (mix of 6, 15, 40+ chars)

**Key rule**: In every paragraph of 100+ chars, include at least one sentence under 8 chars and one over 35 chars.

### Strategy 2: Eliminate AI Template Phrases

**Problem**: Certain phrases are AI generation fingerprints.

**Banned phrases (never use)**:
| AI Template | Human Alternative |
|---|---|
| 本研究旨在 | Direct statement or question |
| 研究表明 / 结果表明 | Directly state the data |
| 综上所述 | Remove entirely or use "说到底" |
| 此外 / 然而 / 因此 (as transitions) | "那""问题是""坦率讲" |
| 需要特别强调的是 | Remove, just say it |
| 值得注意的是 | Remove |
| 这一结果支持了 | "拿到了支持" or just state conclusion |
| 在...的基础上 | Restructure entirely |
| 对...具有重要的...意义 | Simplify |
| 这一发现表明 | Remove, let data speak |
| 从...的角度来看 | Remove or restructure |
| It is worth noting that | Remove |
| This study aims to | Direct statement |
| The results indicate | State the data directly |
| In conclusion | Remove or restructure |
| Furthermore / Moreover / However | "The thing is" / "Problem is" / "Frankly" |

### Strategy 3: Break Parallel Structures

**Problem**: AI loves "第一，...第二，...第三，..." or "一方面...另一方面..." uniform parallel structures.
**Fix**: Make parallel items deliberately uneven—one detailed with examples, one terse, one personal.

- Before: "第一，重新审视权重。第二，增加行为型评估。第三，对评委培训。第四，建立跟踪机制。" (uniform)
- After: "权重要重新看——这点笔者跟选拔组提过两次。面试评分表里'目标清晰度'那栏的权重该压。行为型评估可以加，第二届选拔加了项目测试和黑客松，方向对。至于评委培训..." (uneven, with personal context)

### Strategy 4: Inject Personal Voice and Operational Details

**Problem**: AI writes in passive, objective, impersonal tone.
**Fix**: Add first-person observations, operational difficulties, and emotional reactions.

Examples of personal voice injection:
- "笔者编码920份文本时反复看到的画面是——"
- "这个比例笔者复核了三遍"
- "一开始试过切三档，太粗，后来改成五档才清楚"
- "笔者盯着输出看了挺久"
- "坦率讲，有些文本笔者反复读了三遍才做决定"
- "这个问题笔者问了同组评委三次"

**Rule**: Every 3-4 paragraphs should contain at least one sentence with personal operational detail.

### Strategy 5: Data Embedding (Not Data Listing)

**Problem**: AI presents each statistical result in its own sentence, creating a uniform data-paragraph.
**Fix**: Weave multiple data points into narrative sentences with personal reactions between them.

- Before: "C的效应量为d=1.35。五个潜力维度的d值在0.68到0.92之间。C的效应量最大。这表明职业身份清晰度在选拔中被赋予了过高权重。"
- After: "C的组间差距d=1.35，比五个潜力维度中任何一个都猛——那些d在0.68到0.92之间。笔者看到这个数字时第一反应是'会不会编码有系统偏差'，回头查了三遍编码记录才放下心来。"

### Strategy 6: Replace Academic Collocations with Natural Speech

**Problem**: AI uses formal academic collocations that feel "correct" but are statistically AI-frequent.

| Academic (AI-like) | Natural (Human-like) |
|---|---|
| 系统性漏检 | 大概率被漏掉了 |
| 具有显著的独立预测作用 | 仍然管用 / 还在那 |
| 解释力提升了约16个百分点 | 多出来16个百分点 |
| 这一结果支持了假设 | 假设站住了 |
| 存在相当规模的 | 规模不小 |
| 从...的角度来看 | 说到底 |
| 呈现出较大的个体差异 | 差异已经拉开了 |
| 具有突出的区分作用 | 区分度最猛 |
| systematically overlooked | probably got missed |
| has significant independent predictive effect | still does the job |
| explanatory power increased by | added about |

### Strategy 7: Break Abstract Structure

**Problem**: AI abstracts follow "background→gap→method→results→conclusion" template perfectly.
**Fix**: Use question-driven narrative; mix method and results; put the punchline early.

- Before: "本研究旨在检验...是否存在...。研究以...为样本，基于...方法构建...。结果显示..."
- After: "筛人到底在筛什么？这个问题困扰了笔者两年。920份文本，六个编码指标。几个数字抛出来——d=1.35..."

### Strategy 8: Replace Definition Formula

**Problem**: AI writes definitions with "是指..." or "被定义为..." formula.
**Fix**: Explain concepts through examples and contrast, not formal definition.

- Before: "职业身份清晰度是指个体对于未来职业角色、职业方向、发展路径和角色承诺的明确程度。"
- After: "学生对自己未来要干什么职业角色、走什么方向、有没有承诺，到底清楚到什么程度。打分时只认五条硬证据——文本里有没有明确提一个具体职业..."

### Strategy 9: Add Self-Correction and Trial-and-Error

**Problem**: AI text describes methods as if everything worked on the first try.
**Fix**: Show false starts, method adjustments, and real operational difficulties.

- "一开始试过切三档，太粗，低C档里混了太多人，结论模糊得没法看，后来改成五档才清楚"
- "这个判断笔者做了三次复核，仍然这么评"
- "笔者最终定了个规矩：...但坦白说，有几份文本反复读了三四遍，最后靠的是直觉判断多过编码手册"

### Strategy 10: Dilute with Personal Experience Paragraphs

**Problem**: Even after rewriting flagged paragraphs, overall AIGC rate stays high because unflagged paragraphs still have AI patterns.
**Fix**: Insert 2-3 new paragraphs based on personal research experience. These paragraphs:
- Describe specific scenes (interview settings, coding process, data analysis confusion)
- Include concrete details (names, numbers, durations)
- Express genuine uncertainty ("笔者至今没想清楚")
- Are virtually impossible for AIGC detectors to flag

**Placement**: Insert at natural breakpoints—in discussion (after theoretical analysis), in methods (after coding description), in limitations (after standard limitations).

### Strategy 11: Eliminate Meta-Narration

**Problem**: AI tells readers what it's about to do ("本文将从以下几个方面分析...") or what it just did ("上述分析表明...").
**Fix**: Remove all meta-narration. Just present the content directly.

- Delete: "基于上述文献分析，本研究提出以下研究假设："
- Replace with: Direct hypothesis statement or brief transition like "文献翻完，几个假设抛出来。"

### Strategy 12: Imperfect Logic Flow

**Problem**: AI text has perfect logical flow—every sentence naturally follows from the previous one.
**Fix**: Introduce occasional logical jumps, tangential observations, or delayed explanations.

- Start a sentence with a specific case before explaining the general principle
- Insert a parenthetical observation that breaks the main argument's flow
- Delay explaining an abbreviation or term until 2-3 sentences after first use

## Execution Workflow (Iterative Loop with Quality Assurance)

This skill uses an iterative execution loop. Each round applies all rewriting strategies, then performs a quality deviation check against the ideal outcome. The loop runs a minimum of 10 rounds and exits early only when deviation falls below 10%.

```
Round 1 → Rewrite → Quality Check → Deviation ≥ 10%? → Continue
Round 2 → Rewrite → Quality Check → Deviation ≥ 10%? → Continue
...
Round 10 → Rewrite → Quality Check → Deviation < 10%? → Exit
```

**Minimum rounds: 10. Exit condition: deviation < 10%.**

### Step 1: Analyze the AIGC Report
1. Read the AIGC detection report (usually a Word doc with red/purple highlights)
2. Extract all flagged paragraphs with their text, color label, and character count
3. Categorize: red (high AI probability) vs purple (moderate)
4. Calculate: total chars, flagged chars, flag rate
5. Record as `baseline_aigc_rate` for tracking

### Step 2: Prioritize Targets
- **Priority 1**: Red paragraphs over 200 chars (these contribute most to AIGC rate)
- **Priority 2**: Red paragraphs under 200 chars
- **Priority 3**: Purple paragraphs over 200 chars
- **Priority 4**: Purple paragraphs under 200 chars
- **Priority 5**: Unflagged paragraphs that contain banned phrases or uniform sentence length (preventive)

### Step 3: Apply Rewrites (Per-Round)
For each flagged paragraph, apply strategies 1-12 in this order:
1. First pass: Strategies 2, 6, 11 (phrase replacement—fastest impact)
2. Second pass: Strategies 1, 3, 5 (structural changes)
3. Third pass: Strategies 4, 7, 8, 9 (voice and style)
4. Fourth pass: Strategy 10 (add dilution paragraphs, only in rounds 1-3)

**Per-round variation**: In later rounds, shift strategy emphasis based on remaining issues:
- Rounds 1-3: Full 12-strategy application (heavy rewrite)
- Rounds 4-6: Focus on strategies 1, 4, 5, 12 (fine-tuning sentence rhythm and personal voice)
- Rounds 7-10: Focus on strategies 2, 6, 11 (sweep for residual AI phrases) + cross-paragraph consistency check

### Step 4: Add Dilution Paragraphs (Rounds 1-3 only)
Insert 2-3 personal experience paragraphs (each 150-250 chars) at natural breakpoints:
- After theoretical discussion in the introduction
- After coding method description in methods
- After standard limitations in discussion

These paragraphs should:
- Reference specific operational details (numbers, durations, tool names)
- Express genuine confusion or uncertainty
- Include concrete anecdotes from the research process
- Use the most natural, conversational tone in the entire paper

Note: Do NOT add more dilution paragraphs after round 3 to avoid over-diluting the academic content.

### Step 5: Full Document Scan (Per-Round)
After rewriting all flagged paragraphs, scan the ENTIRE document for:
- Remaining AI template phrases (Strategy 2 list)
- Suspiciously uniform sentence lengths (calculate std dev of sentence lengths per paragraph)
- Untouched parallel structures
- Missing personal voice in discussion/conclusion sections
- New AI patterns created by repetitive alternative expressions (e.g., "说到底" used 5+ times)

### Step 6: Quality Deviation Check (Per-Round)

After each round, calculate a **deviation score** comparing the current document against the ideal outcome. The deviation score is composed of 5 dimensions:

| Dimension | Weight | Ideal State | Measurement |
|---|---|---|---|
| AI phrase residual rate | 30% | 0 banned phrases remain | Count of banned phrases found / total paragraphs |
| Sentence length uniformity | 25% | High variance per paragraph | 1 - (avg sentence length std dev per paragraph / ideal std dev of 15) |
| Personal voice coverage | 20% | Every 3-4 paragraphs has personal voice | 1 - (paragraphs with personal voice / total paragraphs × 4) |
| Parallel structure residual | 15% | No perfect parallel structures | Count of uniform parallel structures remaining |
| Meta-narration residual | 10% | Zero meta-narration sentences | Count of meta-narration sentences / total sentences |

**Deviation Score = (AI phrase × 0.30) + (Uniformity × 0.25) + (Voice gap × 0.20) + (Parallel × 0.15) + (Meta × 0.10)**

Score range: 0% (perfect) to 100% (completely AI-like).

### Step 7: Loop Control

```
if round_number < 10:
    log: "Round {round_number}: deviation={deviation_score}%, minimum 10 rounds not yet reached, continuing..."
    → Record issues found in quality check
    → Feed issues into next round's priority list
    → Go to Step 3
else if round_number >= 10 and deviation_score < 10%:
    log: "Round {round_number}: deviation={deviation_score}% < 10%, exit condition met"
    → Proceed to Step 8 (Output)
else if round_number >= 10 and deviation_score >= 10%:
    if round_number < 20:
        log: "Round {round_number}: deviation={deviation_score}%, still above 10%, continuing..."
        → Record issues found in quality check
        → Feed issues into next round's priority list
        → Go to Step 3
    else:
        log: "Round 20 reached. Deviation still {deviation_score}%. Hard stop."
        → Proceed to Step 8 (Output) with warning
```

### Loop Rules Summary

| Rule | Description |
|---|---|
| Hard minimum | Rounds 1-9 always continue regardless of deviation score |
| Exit condition | From round 10 onward, exit when deviation < 10% |
| Hard stop | Round 20: output current version even if deviation ≥ 10% (with warning) |
| Issue feedback | Each round's quality check findings feed into next round's priority targets |
| Strategy shift | Rounds 1-3 heavy rewrite; 4-6 fine-tuning; 7-10 residual sweep + consistency check |
| Dilution cap | New dilution paragraphs only added in rounds 1-3 (max 9 paragraphs total) |

### Step 8: Generate Output
Save the revised document. Report:
- Number of rounds executed
- Final deviation score
- Number of paragraphs rewritten (cumulative across all rounds)
- Number of new paragraphs added
- AIGC rate trajectory: baseline → final (with per-round breakdown)
- Any remaining issues flagged for manual attention

## Paragraph-Level Rewrite Guidelines

### For Abstracts (Most Critical)
- Never use "本研究旨在" or "本文旨在" opening
- Open with a question, anecdote, or direct finding
- Mix data with personal reaction
- End with implications, not "综上所述"
- Target: 400-500 chars, at least 5 sentences under 10 chars

### For Literature Review
- Don't write "X指出...Y进一步提出...Z发现..." chronological list
- Instead: Group by theme, interrupt with personal observations
- Don't use "此外" to connect paragraphs—use thematic transitions

### For Methods
- Don't use numbered "（1）...（2）...（3）..." uniformly
- Mix formal description with operational notes
- Add at least one "笔者在编码/分析时发现..." sentence per method subsection
- Include at least one trial-and-error anecdote

### For Results
- Don't present each result in isolation with "结果显示"
- Group related results together in narrative
- Add personal reaction to surprising findings
- Include "笔者第一反应是...后来查了...才放心"

### For Discussion
- Don't use "第一，...第二，...第三，..." for implications
- Weave implications into narrative with personal context
- Acknowledge uncertainty explicitly
- Reference specific coding/analysis experiences as evidence

### For Conclusion
- Don't use "本研究基于...系统检验了..." template
- Use conversational summary: "把这些发现拼到一起..."
- End with forward-looking uncertainty, not definitive claim
- Target: 200-300 chars, conversational tone

## Verification Checklist

After rewriting, verify each flagged paragraph against this checklist:

- [ ] Contains at least one sentence under 8 chars
- [ ] Contains at least one sentence over 35 chars
- [ ] No banned AI template phrases (Strategy 2 list)
- [ ] At least one personal voice marker ("笔者" + operational detail)
- [ ] No perfect parallel structure (if listing 3+ items, make them uneven)
- [ ] At least one data point embedded in narrative (not standalone)
- [ ] No meta-narration ("本文将..." / "上述分析...")
- [ ] At least one moment of self-correction or uncertainty

## Important Notes

- **Preserve all data accuracy**: Never change statistical values, p-values, or sample sizes
- **Preserve citations**: Keep all (Author, Year) references intact
- **Don't over-colloquialize**: The paper should still read as academic—use oral expressions sparingly and naturally
- **Consistency**: If using "笔者" in one section, use it throughout (or "我们" consistently)
- **Avoid creating new AI patterns**: Don't repeat the same oral expression across multiple paragraphs (e.g., don't use "说到底" in every conclusion sentence)
- **Language**: This skill works for Chinese and English academic papers. Adapt the banned phrases list for the target language.