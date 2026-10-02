:chapter VIII | Risk and Return
:mood Two roads can have the same average length and still not be equally safe.
:desc This chapter defines risk and return and teaches how to measure both with numbers. It moves from the plain idea of a result that may differ from our hopes, through chances and averages, to the standard deviation and the coefficient of variation. The bakery's two product ideas serve as the running example.

> Two bus routes have the same average journey time but not the same safety.

Suppose that you must catch a train at nine o'clock, and that two bus routes lead to the station. On the first route the journey takes 40 minutes every day, with only a small change from day to day. On the second route the journey takes 20 minutes on some days and 60 minutes on others. Over many days the average is 40 minutes on both routes. Which route would you choose?

> Most people choose the steady route, although the averages are equal.

Most people choose the first route. They do so even though the averages are the same. The reason is that the second route sometimes takes 60 minutes, and on those days you miss the train. An average hides this danger. It tells you where the results lie in the middle, but it does not tell you how far they may wander from the middle.

> Investments behave like the two routes, with results that may wander.

Investments behave in the same way. Two investments can offer the same average gain, yet one of them may give results that wander much further from the average. Sundial Bakery now has two product ideas of this kind. Their average returns are equal, but their results are not equally certain. A careful owner needs a way to put a number on this difference.

> The chapter teaches the numbers in a fixed order, from risk to the coefficient of variation.

This chapter gives that number. It first explains what risk is and what kinds of risk exist. It then shows how to calculate a return, and how to describe uncertain returns with chances. Three measures follow: the expected value, the standard deviation, and the coefficient of variation. The bakery's two ideas are compared at the end. You will need the percentages and square roots of Chapter III, and nothing else.

## What Risk Is

### The everyday word and the finance word

> In daily speech, risk means danger, but finance gives it a wider meaning.

In daily speech, the word risk means danger. A person who crosses a busy road takes a risk of injury. Finance uses the word in a wider sense. The danger of a bad result is part of it, but so is the chance of a result that is better than hoped.

@ Risk | The chance that the actual result will differ from the result we hoped for.

> Risk is the chance that the result differs from the hoped-for result.

In finance, **risk** is the chance that the actual result will differ from the result we hoped for. A result that is better than hoped is a difference, and so is a result that is worse. Both are risk. People usually worry more about the worse result, and we shall see in Chapter X that this worry has a price. But the measure of risk that we use counts differences in both directions.

> A safe result is one that can be known in advance.

A result with no risk is one that can be known in advance. A bank may promise to pay Tk 8,000 interest on Tk 1,00,000 after one year. If the bank keeps its promise, the owner knows the result today. A new line of cakes is different. The sales may be low, fair or high, and the owner cannot know which will occur. The cake line has risk, and the bank promise has almost none.

> Risk is about the future, because the past is already known.

Risk always concerns the future. The sales of last month are known, and they carry no risk. The sales of next month are not known, and they do. This is why risk matters to every decision in this book. The oven of Chapter VII brings in cash over five future years, and each of those yearly sums is an estimate that may prove wrong.

### Kinds of risk

> Risk can be sorted by where it comes from and by what causes it.

Risk can be sorted in more than one way. We use two ways in this book. The first sorts risk by where it comes from: from the whole economy, or from one firm alone. The second sorts risk by its cause inside the firm: the firm's work, or the firm's borrowing. The figure below shows both ways.

:fig Two ways of sorting the risk in a firm's results. The second pair of kinds is only previewed here. | figs/ch8_risk_kinds.svg

@ Market risk | Risk that comes from events affecting all firms, such as a change in interest rates.

> Market risk comes from events that affect every firm at once.

The first kind is **market risk**. It is risk that comes from events that affect all firms together. A rise in interest rates is an example. So is a fall in demand across the whole economy. No single firm causes these events, and no single firm can escape them. For this reason market risk is also called risk that cannot be avoided by choosing a different firm.

@ Firm-specific risk | Risk that comes from events affecting one firm only, such as a fire in its shop.

> Firm-specific risk comes from events that affect one firm alone.

The second kind is **firm-specific risk**. It is risk that comes from events that affect one firm only. A fire in one bakery is an example. So is the departure of the baker whose recipes the shop depends on. Other bakeries are not harmed by these events, and some may even gain from them. An investor who holds shares in many firms is much less hurt by a fire in one of them.

:table Market risk and firm-specific risk compared
| | Market risk | Firm-specific risk |
| --- | --- | --- |
| Whom it affects | All firms | One firm |
| Example | Interest rates rise | A fire in one shop |
| Can an investor avoid it by choosing another firm? | No | Yes, mostly |

> The table sets the two kinds side by side.

The table above sets the two kinds side by side. We have introduced it in words first: the difference lies in how many firms an event touches. Chapter X will show that this difference matters greatly for the return that investors require.

@ Business risk | Risk that comes from the firm's own work, because sales and costs may change.

> Business risk is the risk that the firm's own work brings.

The second way of sorting is a preview of Chapter IX. **Business risk** is the risk that comes from the firm's own work. A bakery's sales may rise or fall, and the price of flour may change. These changes make the firm's profit uncertain before any loan is considered. A bakery that has no debt still has business risk.

@ Financial risk | The extra risk that comes from borrowing money, because interest must be paid in any case.

> Financial risk is the extra risk that borrowing adds.

**Financial risk** is the extra risk that comes from borrowing. A firm that has borrowed must pay interest whether its sales are good or bad. This fixed duty makes the owners' profit swing more widely. Chapter IX measures both kinds of risk. For now it is enough to know that they exist, and that they are different from market risk and firm-specific risk. They describe the same total risk, cut in a different way.

> Other names for risk are special cases of the two ways of sorting.

Books and newspapers use many other names for risk. Interest-rate risk is the risk that a change in interest rates will alter the value of an investment. Inflation risk is the risk that rising prices will reduce what money can buy. Default risk is the risk that a borrower will not repay a loan. Liquidity risk is the risk that an investment cannot be sold quickly without a loss. Each of these fits into the two ways of sorting. The first two usually come from the whole economy, and so they are market risks. Default risk and liquidity risk often belong to one borrower or one investment, and so they are firm-specific.

### Why risk matters

> A careful owner asks for more reward when the risk is greater.

Why should an owner care about risk? Most people prefer a steady result to an uncertain one when the averages are equal. If an owner is to accept a risky choice, the choice must offer more reward than a safe one. How much more is a question for Chapter X. In this chapter we learn first to measure the amount of risk, because nothing can be priced until it has been measured.

## Return and How to Find It

### What return means

> An investment is judged by what it gives back compared with what it cost.

An owner who places money in an investment wants to know what it gave back. The gain in taka is one answer, but it is hard to compare. A gain of Tk 5,000 is large on an investment of Tk 20,000 and small on an investment of Tk 5,00,000. We therefore compare the gain with the cost.

@ Return | The gain on an investment, shown as a share of its cost.

> The return is the gain written as a share of the cost.

The **return** on an investment is the gain that it brings, written as a share of what it cost. The gain has two parts. One part is the income received while the investment is held, such as a dividend or interest. The other part is the change in the value of the investment, which may be a rise or a fall.

@ Rate of return | The return stated as a percentage for one period, usually one year.

> The rate of return states the return as a percentage for one period.

When we state the return as a percentage for one period, usually one year, we call it the **rate of return**. In this chapter we write return for both, and we state it as a percentage. The formula in words is: return equals the money received back, plus any income, minus the money paid, all divided by the money paid.

> The formula is the gain divided by the cost.

In symbols, let P0 be the price paid at the start, P1 the value at the end, and I the income received during the period. Then return = (P1 + I − P0) ÷ P0. The top of the fraction is the gain, which may be negative. The bottom of the fraction is the cost.

### A first example with clean numbers

> A share bought for Tk 200 shows the method with easy numbers.

*Given.* A person buys a share for Tk 200. During the year the share pays a dividend of Tk 10. At the end of the year the person sells the share for Tk 214. *Find.* The return for the year. *Formula.* Return equals the closing value plus the income, minus the price paid, divided by the price paid.

> The gain is Tk 24, and Tk 24 on Tk 200 is 12%.

*Steps.* The gain is Tk 214 + Tk 10 − Tk 200 = Tk 24. Return = Tk 24 ÷ Tk 200 = 0.12, which is 12%. *Answer.* The return for the year is 12%. *Check.* The person paid Tk 200 and has Tk 224 in value and cash. Tk 200 grown by 12% is Tk 200 × 1.12 = Tk 224, which agrees.

### A second example with messier numbers

> A loss gives a negative return, and the method is the same.

*Given.* A person buys a share for Tk 85.50. The share pays a dividend of Tk 4.20. The person then sells the share for Tk 80.30. *Find.* The return. *Steps.* The gain is Tk 80.30 + Tk 4.20 − Tk 85.50 = −Tk 1.00. Return = −Tk 1.00 ÷ Tk 85.50 = −0.0117, which is −1.17%.

> The share fell in price, and the dividend only partly made up the fall.

*Answer.* The return is −1.17%, which is a small loss. The share fell by Tk 5.20 in price, and the dividend of Tk 4.20 made up most of the fall but not all of it. *Check.* The person has Tk 80.30 in value and Tk 4.20 in cash, which is Tk 84.50. This is less than the Tk 85.50 paid, so the return must be negative.

> An investment with no price change, such as a deposit, has a return equal to its interest.

A bank deposit shows the simplest case. A person deposits Tk 50,000 and receives Tk 3,500 as interest after one year. The value at the end is Tk 50,000, so the closing value equals the price paid, and the only gain is the income. Return = Tk 3,500 ÷ Tk 50,000 = 0.07, which is 7%. Interest is a return in the same way as a dividend is.

### Past return and future return

> We can measure a past return exactly, but a future return is uncertain.

The two examples measured returns that are already known. A return that lies in the past can be found exactly, and it has no risk. A return that lies in the future is another matter. The owner can only estimate it, and the estimate may prove wrong. The rest of this chapter teaches how to describe such an uncertain future return with numbers. The first tool for this is the idea of chance.

> Three slips are common when finding a return.

Three slips are common with returns. The first is to leave out the income, and to count only the change in price. The second is to divide the gain by the closing value instead of the price paid. The third is to forget the period: a return of 12% earned in six months is not the same as a return of 12% earned in a year.

## Probability and Probability Distributions

### Chance in numbers

@! Go slowly here. The ideas of chance and of a list of outcomes are new.

> A coin and a die let us learn chance with simple cases.

An owner cannot know next month's sales, but may be able to say how likely each result is. We need a way of writing down likelihood as a number. A coin and a die are the best places to learn it, because their results are easy to count.

@ Probability | A number from 0 to 1 that shows how likely an event is.

> A probability is a number from 0 to 1 that shows how likely an event is.

The **probability** of an event is a number from 0 to 1 that shows how likely the event is. A probability of 0 means that the event cannot happen. A probability of 1 means that it is certain. A fair coin falls heads with a probability of 0.5, because the two sides are equally likely and only one of them is heads. A fair die shows a six with a probability of 1 ÷ 6, which is about 0.17.

> The probabilities of all possible outcomes must add up to exactly one.

One rule governs all probabilities. If we list every possible outcome of an event, the probabilities of the outcomes must add up to exactly 1, because one of them must happen. For the die, six outcomes each have a probability of 1 ÷ 6, and 6 × (1 ÷ 6) = 1. The probability of an even number is the probability of 2, 4 or 6, which is 3 ÷ 6 = 0.5.

### Where the chances come from

> Probabilities for a business come from past records or from judgement.

A coin has a known probability, but a bakery's sales do not. Where do the chances come from? There are two sources. The first is past records. If the cake line had been tried on 40 working days, and sales were weak on 10 days, fair on 20 days and strong on 10 days, the chances would be 10 ÷ 40 = 0.25, 20 ÷ 40 = 0.50 and 10 ÷ 40 = 0.25. The second source is judgement, when no records exist.

> Business probabilities are estimates, so the results must be used with care.

A business probability is always an estimate. The future need not copy the past, and two owners may judge the same facts differently. The calculations that follow are exact, but their inputs are not. This is why the results must be used with care, and why a careful owner tests how much the answer changes when an estimate changes.

### The probability distribution

@ Probability distribution | A list of all possible outcomes, each shown with its chance.

> A probability distribution lists every outcome with its chance.

We now join the outcomes and their chances in one list. A **probability distribution** is a list of all possible outcomes, each shown with its chance. The chances must add up to 1. For the bakery, each outcome is a possible return on the product idea.

:table The bakery's two product ideas: possible returns and their chances
| Outcome | Cake line: return | Cake line: chance | Café corner: return | Café corner: chance |
| --- | --- | --- | --- | --- |
| Weak | 8% | 0.25 | 0% | 0.25 |
| Fair | 12% | 0.50 | 12% | 0.50 |
| Strong | 16% | 0.25 | 24% | 0.25 |
| Total of chances | | 1.00 | | 1.00 |

> Both ideas have the same chances, but different possible returns.

Both ideas have the same chances: a quarter for the weak outcome, a half for the fair outcome, and a quarter for the strong outcome. The possible returns differ. The cake line's returns lie close together, from 8% to 16%. The café corner's returns lie far apart, from 0% to 24%. The next two sections turn these lists into single numbers.

> A missing chance is found by subtracting the known chances from one.

If one chance is missing from a list, we find it by subtraction, because the chances must add up to 1. Suppose that a list has three outcomes, and that two of the chances are 0.2 and 0.5. Their total is 0.7, so the third chance is 1 − 0.7 = 0.3. The same step is a good check on any list that someone else has given us.

## Expected Value

### The average that takes chances into account

> The plain average ignores chances, so we weight each outcome by its chance.

An ordinary average gives every outcome the same weight. But an outcome that is likely should count for more than one that is not. We therefore weight each outcome by its probability, and add the results. This gives the average that we should expect over many repeated trials.

@ Expected value | The average of all possible outcomes, each weighted by its probability.

> The expected value is the average with each outcome weighted by its chance.

The **expected value**, or EV, is the average of all possible outcomes, each weighted by its probability. In words: multiply each outcome by its chance, and add the results. In symbols, EV = p1 × x1 + p2 × x2 + ... + pn × xn, where x is an outcome and p is its probability. We write the same quantity as the expected return when the outcomes are returns.

> The expected value of a die is 3.5, a value that never occurs.

The die shows the idea. Its outcomes are 1 to 6, each with the chance 1 ÷ 6. The expected value is (1 + 2 + 3 + 4 + 5 + 6) ÷ 6 = 3.5. No throw of a die ever shows 3.5. The expected value need not be a possible outcome. It is the average over many throws, and not a prediction of the next throw.

### A first example with clean numbers

> A two-outcome case shows the method with the fewest numbers.

*Given.* An investment may return 20% with a probability of 0.6, or 5% with a probability of 0.4. *Find.* The expected return. *Formula.* Multiply each return by its chance, and add.

> The weighted returns are 12% and 2%, which give 14%.

*Steps.* 0.6 × 20% = 12%. 0.4 × 5% = 2%. EV = 12% + 2% = 14%. *Answer.* The expected return is 14%. *Check.* The answer lies between the two returns, 5% and 20%. It lies nearer to 20%, which has the larger chance, and the chances add up to 0.6 + 0.4 = 1.

> The figure shows the expected value as the balance point of the outcomes.

The figure below shows a useful picture. Imagine the outcomes as weights on a beam, each placed at its return, and each weight proportional to its chance. The expected value is the point at which the beam balances. The larger weight at 20% is balanced by the smaller weight at 5%, which is farther from the balance point.

:fig The expected value as a balance point. The weight of 0.6 at 20% and the weight of 0.4 at 5% balance at 14%. | figs/ch8_balance.svg

### A second example with messier numbers

> The cake line has three outcomes, and the method is the same.

Now the bakery's ideas, with three outcomes each. *Given.* The distribution of the cake line is in the table of the last section. *Find.* The expected return of each idea. *Steps.* For the cake line: 0.25 × 8% = 2%, then 0.50 × 12% = 6%, then 0.25 × 16% = 4%. The total is 12%. For the café corner: 0.25 × 0% = 0%, then 0.50 × 12% = 6%, then 0.25 × 24% = 6%. The total is 12%.

> Both ideas have the same expected return of 12%.

*Answer.* The expected return is 12% for both the cake line and the café corner. *Check.* In each list the outcomes are spread evenly on both sides of 12%, with equal chances. The balance point must therefore be 12%, and it is.

> The expected value cannot tell the two ideas apart.

Here lies the difficulty that began the chapter. The two ideas have the same expected value, so the expected value cannot separate them. Yet the café corner may return nothing and the cake line cannot. We need a second number, one that measures how far the outcomes wander from the expected value.

### A third example with a loss in the list

> An outcome may be negative, and the method does not change.

*Given.* A project may return −10% with a chance of 0.2, 10% with a chance of 0.5, or 30% with a chance of 0.3. *Find.* The expected return. *Steps.* 0.2 × (−10%) = −2%. 0.5 × 10% = 5%. 0.3 × 30% = 9%. EV = −2% + 5% + 9% = 12%. *Answer.* The expected return is 12%, although one of the outcomes is a loss. *Check.* The chances add up to 0.2 + 0.5 + 0.3 = 1, and the answer lies between the lowest and the highest outcome.

> Three slips are common when finding an expected value.

Three slips are common. The first is to take the plain average of the outcomes and ignore the chances. The second is to use chances that do not add up to 1. The third is to treat the expected value as a promise. It is an average over many trials, and a single trial can give any of the outcomes.

## Standard Deviation

### Measuring the wandering

@! Go slowly here. This is the hardest calculation of the chapter, and it has five steps.

> We want one number for how far outcomes lie from the expected value.

We want one number that shows how far the outcomes wander from the expected value. A natural first step is to find, for each outcome, its distance from the expected value. This distance is called the deviation. A deviation is positive when the outcome lies above the expected value, and negative when it lies below.

> Deviations cannot be averaged as they stand, because they cancel one another.

If we weight the deviations by their chances and add them, the positive and negative ones cancel, and the total is zero. For the two-outcome case, 0.6 × 6% + 0.4 × (−9%) = 3.6% − 3.6% = 0. The total is zero for every distribution, so it tells us nothing. The remedy is to square each deviation before the weighting, because a square is never negative.

@ Variance | The average of the squared deviations from the expected value, each weighted by its chance.

> The variance is the weighted average of the squared deviations.

The **variance** is the average of the squared deviations from the expected value, each weighted by its probability. A larger variance means that the outcomes lie farther from the expected value. The variance has one inconvenience. If the outcomes are in per cent, the variance is in per cent squared, which is hard to picture.^1

> Taking the square root brings the measure back to the original unit.

We return to the original unit by taking the square root of the variance. The result is the standard measure of spread.

@ Standard deviation | The square root of the variance; the usual distance of outcomes from the expected value.

> The standard deviation is the square root of the variance.

The **standard deviation**, or SD, is the square root of the variance. It is the usual distance of the outcomes from the expected value, stated in the same unit as the outcomes. A large standard deviation means that the results often lie far from the expected value, and so the risk is large. A small one means that they lie close, and the risk is small.

^1: When a standard deviation is found from a list of past observations and not from chances, books divide the sum of squares by the number of observations, or by one fewer. This chapter uses chances only, so no such division arises.

### The five steps

> The calculation follows five fixed steps, in the same order every time.

The calculation always follows five steps. First, find the expected value. Second, find each deviation, which is the outcome minus the expected value. Third, square each deviation. Fourth, multiply each squared deviation by its chance, and add the results. This sum is the variance. Fifth, take the square root of the variance. Use the calculator for the square root, as Chapter III showed.

### A first example with clean numbers

> The two-outcome investment gives a standard deviation of about 7.35%.

*Given.* The investment of the last section: 20% with a probability of 0.6, and 5% with a probability of 0.4. The expected return is 14%. *Find.* The standard deviation.

:table Standard deviation of the two-outcome investment
| Return | Chance | Deviation | Squared deviation | Chance × squared deviation |
| --- | --- | --- | --- | --- |
| 20% | 0.6 | 6 | 36 | 21.6 |
| 5% | 0.4 | −9 | 81 | 32.4 |
| Variance | | | | 54.0 |

> The variance is 54, and its square root is the standard deviation.

The variance is 21.6 + 32.4 = 54.0, in per cent squared. The standard deviation is the square root of 54, which is 7.35%. *Answer.* The standard deviation is about 7.35%. *Check.* The deviations are 6 and −9, so a usual distance between them, about 7, is sensible. A result of 7.35% lies between 6 and 9, as it should.

### A second example with messier numbers

> The bakery's two ideas have very different standard deviations.

Now the two ideas of the bakery, each with an expected return of 12%. For the cake line, the deviations are 8 − 12 = −4, 12 − 12 = 0 and 16 − 12 = 4. For the café corner, they are 0 − 12 = −12, 0 and 24 − 12 = 12.

:table Standard deviation of the two product ideas
| | Cake line | Café corner |
| --- | --- | --- |
| Deviations (weak, fair, strong) | −4, 0, 4 | −12, 0, 12 |
| Squared deviations | 16, 0, 16 | 144, 0, 144 |
| Each times its chance (0.25, 0.50, 0.25) | 4, 0, 4 | 36, 0, 36 |
| Variance | 8 | 72 |
| Standard deviation | 2.83% | 8.49% |

> The café corner's standard deviation is three times the cake line's.

The cake line has a variance of 8 and a standard deviation of √8 = 2.83%. The café corner has a variance of 72 and a standard deviation of √72 = 8.49%. *Answer.* The standard deviations are 2.83% and 8.49%. *Check.* Every deviation of the café corner is three times the matching deviation of the cake line, so its standard deviation must be three times as large. 2.83 × 3 = 8.49, which agrees.

> The figure shows the same two ideas as pictures.

The figure below shows the two distributions as bars. They have the same centre, 12%, and the same chances. But the café corner's bars lie much farther apart. The standard deviation measures exactly this difference.

:fig The two product ideas. Both have an expected return of 12%, but the café corner's outcomes are spread much more widely. | figs/ch8_distributions.svg

### A third example with unequal chances

> An uneven distribution shows that the five steps still hold.

The five steps work for any distribution, including one whose chances are unequal. Use the project of the last section, with returns of −10%, 10% and 30%, chances of 0.2, 0.5 and 0.3, and an expected return of 12%. The deviations are −10 − 12 = −22, 10 − 12 = −2 and 30 − 12 = 18. The squared deviations are 484, 4 and 324. Weighted by the chances, they are 0.2 × 484 = 96.8, 0.5 × 4 = 2.0 and 0.3 × 324 = 97.2.

> The variance is 196 and the standard deviation is 14%.

The variance is 96.8 + 2.0 + 97.2 = 196.0. The standard deviation is the square root of 196, which is 14%. *Answer.* The standard deviation is 14%. *Check.* The outcomes lie 22, 2 and 18 points from the expected value, and the largest chance, 0.5, belongs to the outcome that lies closest. A usual distance of 14 points is therefore sensible.

### Reading the standard deviation

> A standard deviation is a usual distance, and not a limit.

How should we read a standard deviation? The cake line's 2.83% means that its returns usually lie within about three points of 12%. It is a usual distance, and not a limit. A result farther from the expected value is possible, and for some distributions it is quite likely. We should not read the standard deviation as the greatest loss that can occur.

> Four slips are common when finding a standard deviation.

Four slips are common. The first is to forget to square the deviations. The second is to forget to multiply by the chances. The third is to forget the final square root, and to report the variance as if it were the standard deviation. The fourth is to mix units, by using 0.12 for one outcome and 12 for another. A check that the answer lies near the size of the deviations will find most of these slips.

## The Coefficient of Variation

### Comparing choices that do not have equal averages

> When the expected values are equal, the smaller standard deviation is the safer choice.

When two choices have equal expected returns, the comparison is easy. The choice with the smaller standard deviation has less risk. This is the case for the cake line and the café corner, and the cake line has the smaller standard deviation of 2.83%. But the expected returns of two choices are often unequal, and then the standard deviation alone can mislead.

> A larger standard deviation may be fair if the expected return is larger as well.

Suppose that investment X has an expected return of 10% and a standard deviation of 4%. Investment Y has an expected return of 20% and a standard deviation of 6%. Y has the larger standard deviation, but it also offers a much larger expected return. To compare them fairly we need to know how much risk each one carries for each unit of expected return.

@ Coefficient of variation | The standard deviation divided by the expected value; the risk taken for each unit of expected return.

> The coefficient of variation divides the risk by the expected return.

The **coefficient of variation**, or CV, is the standard deviation divided by the expected value. It states the risk taken for each unit of expected return. In symbols, CV = SD ÷ EV. A smaller CV means less risk for each unit of return. The CV has no unit, because the unit of the numerator and that of the denominator cancel.

### An example with unequal averages

> The CV of X is 0.40 and the CV of Y is 0.30, so Y carries less risk per unit.

*Given.* Investment X: expected return 10%, standard deviation 4%. Investment Y: expected return 20%, standard deviation 6%. *Find.* The CV of each, and which carries less risk for each unit of return. *Steps.* CV of X = 4 ÷ 10 = 0.40. CV of Y = 6 ÷ 20 = 0.30. *Answer.* Y has the smaller CV, so it carries less risk for each unit of expected return, although its standard deviation is larger. *Check.* Y's expected return is twice X's, and its standard deviation is only one and a half times X's, so Y's ratio must be smaller.

### The bakery's two ideas

> The cake line's CV is 0.24, and the café corner's is 0.71.

Now apply the CV to the bakery. For the cake line, CV = 2.83 ÷ 12 = 0.24. For the café corner, CV = 8.49 ÷ 12 = 0.71. The expected returns are equal, so the CV ranks the ideas in the same order as the standard deviation does. The café corner carries about three times as much risk for each unit of return as the cake line.

> A third project shows what a high coefficient of variation looks like.

The project of the last section has an expected return of 12% and a standard deviation of 14%, so its CV is 14 ÷ 12 = 1.17. Its spread is larger than its expected return. Compare this with the cake line's 0.24. A CV above 1 shows that the risk for each unit of return is high, and a careful owner would ask for a strong reason before accepting such a project.

> The CV has limits that a careful student should know.

The CV has one limit. If the expected value is close to zero, the CV becomes very large, and if it is negative, the CV has no clear meaning. In such cases the standard deviation should be examined by itself. Another point is that the CV measures the amount of risk, but it does not tell the owner how much risk to accept. That depends on how much extra reward the owner asks. Chapter X deals with it.

## The Worked Case: Cake Line or Café Corner

> The case file records the two ideas, their returns and their chances.

:case Case file, illustrative. Sundial Bakery, Dhaka. The owner considers two product ideas for the shop. The cake line is estimated to return 8%, 12% or 16%, with chances of 0.25, 0.50 and 0.25. The café corner is estimated to return 0%, 12% or 24%, with the same chances. The chances come from the owner's judgement, helped by the sales records of the first months.

> We state what is given and what the owner must find.

*Given.* The two distributions above. *Find.* The expected return, the standard deviation and the coefficient of variation of each idea, and a statement of which is riskier. *Formula.* EV is the sum of each outcome times its chance. Variance is the sum of each squared deviation times its chance. SD is the square root of the variance. CV is SD divided by EV.

> The steps give the same expected return and different spreads.

*Steps.* For the cake line, EV = 0.25 × 8 + 0.50 × 12 + 0.25 × 16 = 2 + 6 + 4 = 12%. The variance is 0.25 × 16 + 0.50 × 0 + 0.25 × 16 = 8, and SD = 2.83%. CV = 2.83 ÷ 12 = 0.24. For the café corner, EV = 0 + 6 + 6 = 12%. The variance is 0.25 × 144 + 0 + 0.25 × 144 = 72, and SD = 8.49%. CV = 8.49 ÷ 12 = 0.71.

:table The two product ideas on three measures
| Measure | Cake line | Café corner |
| --- | --- | --- |
| Expected return | 12% | 12% |
| Standard deviation | 2.83% | 8.49% |
| Coefficient of variation | 0.24 | 0.71 |

> The café corner is riskier by every measure, though the average return is equal.

*Answer.* The two ideas have the same expected return of 12%. The café corner is riskier on both measures: its standard deviation is 8.49% against 2.83%, and its coefficient of variation is 0.71 against 0.24. *Check.* The probabilities of each idea add up to 1. Each expected value lies in the middle of its outcomes, as the symmetric chances require. The café corner's spread is exactly three times the cake line's, as its deviations are.

> Which idea to choose depends on the reward the owner asks for risk.

The measures do not tell the owner what to choose. They tell the owner what each choice means. With equal expected returns, a cautious owner prefers the cake line, because it offers the same average with less wandering. The owner would choose the café corner only if it promised a higher expected return, enough to pay for its extra risk. Chapter X shows how to put a price on that difference.

> The measures also bear on the oven and the van of Chapter VII.

These measures return in Chapter X. They also bear on the choices of Chapter VII. The yearly cash flows of the oven were single estimates. In truth each could turn out higher or lower, so the oven's NPV also has a spread. An owner who wished to know how safe the oven's NPV of Tk 79,079 is would describe the possible sales with chances, as we did for the product ideas. We do not carry out that work here.

## Summary

> The measures of the chapter in a few lines.

Risk is the chance that the actual result differs from the hoped-for result. Market risk affects all firms, and firm-specific risk affects one. Business risk and financial risk sort the same total risk by its cause inside the firm. Return is the gain on an investment as a share of its cost. Probability is a number from 0 to 1, and a probability distribution lists the outcomes with chances that add up to 1. The expected value is the weighted average of the outcomes. The standard deviation is the square root of the weighted average of the squared deviations, and it measures the spread. The coefficient of variation divides the standard deviation by the expected value, and it compares risk per unit of return.

> You should now be able to say how each measure is found and used.

You should now be able to say: the expected value shows where the outcomes centre, the standard deviation shows how far they wander, and the coefficient of variation shows the risk for each unit of return. You should also be able to find all three from a list of outcomes and chances.

## Think It Through

> Two investments with unequal averages give the reader a case to analyse.

:case Case file, illustrative. The owner of Sundial Bakery is offered two investments for spare cash. Investment M may return 4%, 10% or 16%, with chances of 0.3, 0.4 and 0.3. Investment N may return −5%, 15% or 35%, with chances of 0.2, 0.6 and 0.2.

> The questions ask for the three measures and a comparison.

Find the expected return, the standard deviation and the coefficient of variation of each investment. Say which investment is riskier by the standard deviation, and which carries more risk for each unit of expected return. Explain why the two answers may or may not be the same. Then find the return on a share that is bought for Tk 150, pays a dividend of Tk 6, and is sold for Tk 141.

## Where People Go Wrong

> Mistake: believing that risk means only the chance of loss.

*Mistake:* believing that risk is only the chance of a loss. *Correction:* in finance, risk is the chance of any difference from the hoped-for result, in either direction. The standard deviation counts both.

> Mistake: using chances that do not add up to one.

*Mistake:* using probabilities that total more or less than 1. *Correction:* a complete list of outcomes must have chances that add up to exactly 1. Add them before any other step.

> Mistake: taking the plain average of the outcomes.

*Mistake:* averaging the outcomes without weights. *Correction:* each outcome must be multiplied by its chance, so that likely outcomes count for more.

> Mistake: stopping at the variance.

*Mistake:* reporting the variance as the standard deviation. *Correction:* the standard deviation is the square root of the variance. The variance is in squared units, and the standard deviation is in the original unit.

> Mistake: comparing standard deviations when the expected returns differ.

*Mistake:* choosing the investment with the smaller standard deviation when the expected returns are not equal. *Correction:* compare the coefficients of variation, which state the risk for each unit of expected return.

> Mistake: reading the expected value as a promise.

*Mistake:* expecting the expected return to occur. *Correction:* the expected value is an average over many trials. A single trial gives one of the outcomes, and it may be far from the average.

## In History

> Harry Markowitz put the expected return and the variance to work in 1952.

In 1952 the American economist Harry Markowitz published a paper called *Portfolio Selection* in the *Journal of Finance*. In it he proposed that an investor should describe each investment by two numbers: its expected return and the variance of its return. He argued that investors should look at the two together, and that holding several investments can reduce risk without lowering the expected return. Later writers developed these ideas into the theory that Chapter X will introduce.

## Sources

> A short note on the origin of the ideas in this chapter.

Harry Markowitz, *Portfolio Selection*, *Journal of Finance* (1952), is the landmark source for describing an investment by its expected return and the variance of its return. The measures of probability, expected value and standard deviation are standard topics in textbooks of statistics and of financial management.

## Review Questions

> Risk and its kinds.

1. Define risk as the word is used in finance. Then explain the difference between market risk and firm-specific risk, with one example of each.

> Classifying events.

2. Say whether each event is mainly a market risk or a firm-specific risk: a fire at one bakery, a rise in interest rates across the country, a rival shop that opens next door.

> Return.

3. A share is bought for Tk 250, pays a dividend of Tk 10, and is sold for Tk 235. Find the return for the period, and say whether it is a gain or a loss.

> Probability.

4. A project may return 4%, 9% or 17%. The chances of the first two outcomes are 0.30 and 0.45. Find the chance of the third outcome, and then find the expected return.

> Standard deviation.

5. A project may return 2%, 8% or 14%, with chances of 0.25, 0.50 and 0.25. Find its expected return, its variance and its standard deviation.

> Coefficient of variation.

6. Asset G has an expected return of 15% and a standard deviation of 6%. Asset H has an expected return of 9% and a standard deviation of 3%. Find the coefficient of variation of each, and say which has less risk for each unit of return.

> Why the average is not enough.

7. Explain why the expected value alone is not enough to compare two investments. Use the idea of the two bus routes, or an example of your own.

> Reading the measures.

8. Two investments have equal expected returns. One has a standard deviation of 3% and the other has a standard deviation of 9%. Which is riskier, and what extra thing would a cautious owner ask of the riskier one?
