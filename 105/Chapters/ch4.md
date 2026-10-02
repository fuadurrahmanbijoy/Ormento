:chapter IV | Money Over Time: Single Sums
:mood Is a taka today worth the same as a taka next year?
:desc This chapter teaches that a taka now and a taka later are different things, and shows how to move one sum of money forward and backward through time. We learn future value, present value, and the tables that make the work quick.

> A friend offers Tk 1,00,000 today or Tk 1,00,000 in a year.
A friend offers you a choice. You may take Tk 1,00,000 today, or you may take Tk 1,00,000 in exactly one year. The friend is honest and will certainly pay. Almost everyone chooses today. Why? The two amounts are equal, and yet no sensible person treats the two offers as equal.

> Now the later offer is larger, and the choice is no longer easy.
Make the offer harder. You may take Tk 1,00,000 today, or Tk 1,10,000 in one year. The later sum is larger by Tk 10,000. Is it better to wait? The answer depends on something we have not yet named: what the Tk 1,00,000 could earn in the meantime. Different people, with different opportunities, will answer differently, and both can be right.

> The bakery faces such questions on 1 April 2026.
The bakery faces such questions on 1 April 2026. After its first quarter, the owner has Tk 1,00,000 of spare cash, and a bank offers 8% a year. The owner also knows that equipment will need replacing in five years, at a cost of Tk 2,00,000. How much will the spare cash be worth in three years? How much must be set aside today to meet the replacement cost? Each question asks us to move money through time.

> Sums at different dates must be brought to one date before they are compared.
Money at different dates cannot be compared directly, as kilograms cannot be added to litres. We must first bring both sums to the same date. This chapter teaches how: moving one sum forward in time, moving one sum backward, and doing both quickly with tables. The idea behind it has a name, which we meet in section 4.1. It is the most important idea in finance, and the rest of the book stands on it. So we shall move slowly.

> You will need the arithmetic of Chapter III.
*You will need:* percentages, powers and roots, the order of operations, and the reading of tables, all from Chapter III. If any of these feels uncertain, read sections 3.1 to 3.3 again before going on. The words interest, saving and borrowing come from Chapter I.

## 4.1 Why Time Matters

@! Go slowly here.
> Everyday bridge: a neighbour owes you Tk 1,000 and offers two ways to pay.
Imagine that a neighbour owes you Tk 1,000. She offers to pay today. Or she says, "I will pay you next year, and I promise." Which do you prefer? Most people answer, "Today." Ask them to explain, and three reasons usually appear. We take them one at a time, because each reason teaches something.

> First reason: money in hand can earn interest.
The first reason is that money received today can be put to work. You could place Tk 1,000 in a bank. After a year the bank would return your Tk 1,000 and add interest. Recall from Chapter I that interest is a fee for using someone's money. If you wait a year for your Tk 1,000, you lose the interest that you could have earned. Waiting has a cost.

> Second reason: prices usually rise, so money buys less later.
The second reason is that prices usually rise. A box of buns that costs Tk 40 today may cost Tk 42 next year. Then Tk 1,000 next year buys fewer boxes than Tk 1,000 today. The money is the same, but what it can buy is smaller.

> Third reason: a promise may be broken.
The third reason is uncertainty. A promise about next year may fail, because the neighbour may be unable to pay. Money in hand is certain, and money promised is not. Chapter VIII studies this reason. In this chapter we remove it by assuming that every future payment is certain. Then we can study the first reason, which is the heart of finance.

@ Time value of money | The idea that a taka now is worth more than a taka later.
> These reasons together give the idea its name: the time value of money.
The three reasons together give an idea its name. The **time value of money** means that a taka now is worth more than a taka later. Notice what the idea does not say. It does not say that a later taka is worthless. It says that a later taka is worth *less than a taka today*, and that we can state by how much.

@ Interest rate | The interest for one year, shown as a percentage of the sum lent.
> The interest rate is the tool that measures the difference between now and later.
Interest is the tool for measuring this difference. The **interest rate** means the interest for one year, shown as a percentage of the sum lent. If the rate is 10% a year, then Tk 100 lent today earns Tk 10 in a year. So Tk 100 today and Tk 110 in a year are *equal in value* to a person who can earn 10%. That person has no reason to prefer one to the other. This small comparison is the seed of the whole chapter.

> First worked example, with the smallest numbers: Tk 100 at 10%.
*Given.* A sum of Tk 100 today, and an interest rate of 10% a year. *Find.* The sum, one year from now, that is worth the same as Tk 100 today. *Formula.* Sum after one year = sum today + interest, and interest = sum today × rate. *Steps.* Interest = 100 × 10% = Tk 10. Sum after one year = 100 + 10 = Tk 110. *Answer.* Tk 100 today is worth the same as Tk 110 in one year. *Check.* Lend Tk 100 and, one year later, you hold Tk 110. The two sums are two names for one value at two dates.

@ Timeline | A line that shows the dates at which money moves.
@ Single sum | One payment made at one date.
> To follow money through time, we draw a timeline.
To follow money through time we draw a **timeline**. A timeline means a line that shows the dates at which money moves. We mark today as Year 0. One year from today is Year 1, two years from today is Year 2, and so on. A **single sum** means one payment made at one date. Every sum in this chapter is a single sum: one amount at one point on the line.

> Fig. 4 shows a timeline and the two directions of movement.
:fig A timeline for Tk 100 at 10% a year. Moving right, the sum grows; moving left, it is brought back. | fig_ch4_timeline.svg

> How to read the timeline figure.
To read Fig. 4, begin at the left with Year 0 and Tk 100. Each step to the right is one year, and the sum grows by 10% at each step: Tk 110.00, Tk 121.00, and Tk 133.10. We call the move to the right *compounding*. Each step to the left brings a sum back by one year. We call the move to the left *discounting*. Sections 4.2 and 4.3 teach each move in turn. Notice that the same rate, 10%, is used in both directions.

> Viewpoint: lender, borrower and owner each see interest differently.
Different seats give different views of the same rate. To the lender, interest is income for waiting. To the borrower, it is the cost of having money early. To the owner of the bakery it is both: a price paid on the bank's loan, and an income when spare cash is placed in a deposit. In each case the rate is the exchange price between today's money and next year's money.

> Two limits: the equal-value statement holds only at a stated rate, and our payments are certain.
Two limits matter. First, the equality of Tk 100 today and Tk 110 in a year holds only if 10% is the right rate. At 5%, Tk 100 would grow to Tk 105 only, and a promise of Tk 110 in a year would then be worth *more* than Tk 100 today. The rate we choose decides the answer. Second, we assume that interest is paid at the end of each year and that all future sums are certain. Later chapters relax these assumptions one at a time.

> Pause and check: lending Tk 200 at 10%.
*Pause and check.* Tk 200 is lent today at 10% a year. How much does the lender hold at Year 1? What sum today is worth the same as Tk 220 at Year 1? The answers are at the back of the book.

> You should now be able to say why a taka now beats a taka later.
*You should now be able to say:* "A taka now is worth more than a taka later, because money can earn interest, and the interest rate tells me by how much."

> A recap of the section.
*Before moving on.* The time value of money says that a taka now is worth more than a taka later, mainly because money can earn interest. A timeline puts dates on money. A single sum is one payment at one date. Moving right on the line is compounding, and moving left is discounting.

## 4.2 Future Value of a Single Sum

> We begin with the bakery's deposit and ask what it becomes.
On 1 April 2026 the owner places Tk 1,00,000 of spare cash in a bank at 8% a year. The owner wants to know what the deposit will be worth in three years. This is a question about moving a sum to the right on the timeline. Before we answer it, we must understand how a bank counts interest, because there are two ways.

@ Simple interest | Interest worked on the first sum only.
@ Compound interest | Interest worked on the first sum and on the interest already added.
> Simple interest is worked on the first sum only; compound interest on the growing sum.
With **simple interest**, the bank works the interest on the first sum only. With **compound interest**, the bank works the interest on the first sum *and* on the interest already added. Take Tk 1,00,000 at 10% for two years. With simple interest, each year brings Tk 10,000, so two years bring Tk 20,000, and the sum is Tk 1,20,000. With compound interest, year 1 brings Tk 10,000 and the sum becomes Tk 1,10,000. Year 2 brings 10% of Tk 1,10,000, which is Tk 11,000, and the sum becomes Tk 1,21,000.

@ Compounding | The process of earning interest on interest already added.
> The extra Tk 1,000 is interest earned on interest.
The two methods differ by Tk 1,000. That is the interest earned in year 2 on the Tk 10,000 of interest from year 1, since 10% of Tk 10,000 is Tk 1,000. The process of earning interest on interest is called **compounding**. Almost all bank deposits and bank loans work this way, so compound interest is the method we shall use from now on unless we say otherwise.

@ Future value | What a sum today grows to at a later date.
@ Present value | What a later sum is worth today. (In daily life, a present can mean a gift.)
> Two names are needed: the sum today is the present value, and the grown sum is the future value.
We need two names. The **future value** means what a sum today grows to at a later date. The **present value** means what a later sum is worth today. In this section we start from a present value and find a future value. In section 4.3 we do the reverse. The word *present* here means "now", and has nothing to do with a gift.

> The year-by-year pattern: each year the sum is multiplied by one plus the rate.
Look at the pattern in the compound case. At the end of year 1, the sum is the first sum multiplied by 1.10. At the end of year 2, it is that sum multiplied by 1.10 again: 1,00,000 × 1.10 × 1.10. Each year multiplies the sum by the same number, one plus the rate. After n years we multiply n times, which is the power of section 3.2. The exponent counts the years.

> The rule for future value, in words and in symbols.
The rule in words: the future value equals the present value multiplied by one plus the interest rate, raised to the power of the number of years. In symbols, FV = PV × (1 + r)ⁿ. Here FV is the future value, PV is the present value, r is the interest rate for one year written as a decimal (so 8% is 0.08), and n is the number of years. The number (1 + r)ⁿ is the multiplier that carries a sum n years forward.

> First worked example of the rule: Tk 1,00,000 at 10% for two years.
*Given.* PV = Tk 1,00,000, r = 10% = 0.10, n = 2 years. *Find.* FV. *Formula.* FV = PV × (1 + r)ⁿ. *Steps.* First, 1 + 0.10 = 1.10. Second, 1.10² = 1.21. Third, FV = 1,00,000 × 1.21 = Tk 1,21,000. *Answer.* The future value is Tk 1,21,000. *Check.* This agrees with the year-by-year count above: Tk 1,10,000 after year 1 and Tk 1,21,000 after year 2.

> Second worked example: the bakery's spare cash at 8% for three years.
*Given.* PV = Tk 1,00,000, placed on 1 April 2026; r = 8% = 0.08; n = 3 years. *Find.* FV on 1 April 2029. *Formula.* FV = PV × (1 + r)ⁿ. *Steps.* First, 1 + 0.08 = 1.08. Second, 1.08² = 1.1664, and 1.1664 × 1.08 = 1.259712, so 1.08³ = 1.259712. Third, FV = 1,00,000 × 1.259712 = Tk 1,25,971.20, which is Tk 1,25,971 to the nearest taka.

> The answer and a check by the year-by-year route.
*Answer.* The deposit will be worth Tk 1,25,971 on 1 April 2029. *Check.* Count year by year: Tk 1,00,000 × 1.08 = Tk 1,08,000; × 1.08 = Tk 1,16,640; × 1.08 = Tk 1,25,971.20. The answer also exceeds the simple-interest answer, Tk 1,00,000 + 3 × Tk 8,000 = Tk 1,24,000, as it should.

> Third worked example: an awkward rate, 9.5% for four years.
*Given.* PV = Tk 60,000, r = 9.5% = 0.095, n = 4 years. *Find.* FV. *Formula.* FV = PV × (1 + r)ⁿ. *Steps.* First, 1 + 0.095 = 1.095. Second, 1.095² = 1.199025. Third, 1.199025² = 1.437661, so 1.095⁴ = 1.437661. Fourth, FV = 60,000 × 1.437661 = Tk 86,259.66, which is Tk 86,260. *Answer.* Tk 86,260. *Check.* With simple interest the sum would be 60,000 + 4 × 5,700 = Tk 82,800, which is smaller than Tk 86,260, as it should be.

> Fig. 5 shows how compounding pulls away from simple interest.
:fig Tk 1,00,000 at 8% a year for ten years. The curve is compound interest; the dashed line is simple interest. | fig_ch4_growth.svg

> How to read the growth figure and what it teaches.
To read Fig. 5, look along the bottom for the years and up the left side for the sum in lakhs of taka. Both lines start at 1.0, which is Tk 1,00,000. The dashed line rises by the same amount each year, because simple interest is always worked on the first sum. The curve rises faster each year, because compound interest is worked on a larger sum each time. After ten years, compounding gives Tk 2,15,892 and simple interest gives Tk 1,80,000.

> The lesson: compounding matters most when time is long.
The figure carries a lesson. In the first two years the two lines are almost the same. After ten years, they are Tk 35,892 apart. Compounding rewards patience, and it punishes a borrower who does not repay. This is why a small difference in the interest rate, or in the length of time, can lead to a very large difference in the sum.

@! Go slowly here.
> Solving for the rate: the rule can be turned round to find the interest rate.
Sometimes we know the present value, the future value and the years, and we want the rate. The rule can be turned round using a root from section 3.2. In words: the rate equals the root of the future value divided by the present value, less 1, where the root is the n-th root and n is the number of years. In symbols, r = (FV ÷ PV)^(1/n) − 1. The exponent 1/n is the instruction to take the n-th root.

> Fourth worked example: finding the rate from two sums.
*Given.* PV = Tk 1,00,000, FV = Tk 1,46,933, n = 5 years. *Find.* r. *Formula.* r = (FV ÷ PV)^(1/n) − 1. *Steps.* First, FV ÷ PV = 1,46,933 ÷ 1,00,000 = 1.46933. Second, raise 1.46933 to the power 1/5 = 0.2. The calculator shows 1.08000. Third, r = 1.08000 − 1 = 0.08000. *Answer.* The rate is 8% a year. *Check.* Raise 1.08 to the power 5: it gives 1.469328, which is the multiplier we began with.

> Solving for the number of years: try year after year until the target is passed.
We can also ask how long a sum takes to reach a target. The simplest method needs no new rule. Keep multiplying by (1 + r) and count the years. *Given.* Tk 1,00,000 grows at 8% a year. *Find.* The time to double. *Steps.* 1.08⁸ = 1.8509, which is below 2. 1.08⁹ = 1.9990, which is still a little below 2. 1.08¹⁰ = 2.1589, which is above 2. *Answer.* The sum doubles in a little more than 9 years. *Check.* Run the calculator to nine years: Tk 1,00,000 × 1.9990 = Tk 1,99,900, which is very near Tk 2,00,000.

> An advanced note for readers who know logarithms, which a beginner may skip.
*Advanced; a beginner may skip this paragraph.* Readers who know logarithms can solve for the years directly: n = ln(FV ÷ PV) ÷ ln(1 + r). For doubling at 8%, ln 2 = 0.693147 and ln 1.08 = 0.076961, so n = 9.006 years. This agrees with the trial method. Section 4.5 shows a third method, using a table.

> Common slips in future value.
Four slips are common. First, writing 8 in the formula instead of 0.08. Second, multiplying by n instead of raising to the power n: 1.08 × 3 = 3.24 is not 1.08³. Third, using n − 1 or n + 1 years, which comes from miscounting the dates on the timeline: from 1 April 2026 to 1 April 2029 is three years. Fourth, mixing the units of the rate and the time. A rate per year goes with years, not months.

> Pause and check: the future value of Tk 50,000.
*Pause and check.* Find the future value of Tk 50,000 invested for four years at 10% a year. Show the given, the formula, the steps and a check. The answer is at the back of the book.

> A recap of the section.
*Before moving on.* Compound interest is worked on the sum and on the earlier interest. The future value of a present value is PV × (1 + r)ⁿ. The rule can be turned round to find the rate, using a root, or to find the years, by trial. You should now be able to say: "Each year multiplies the sum by 1 plus the rate, and the exponent counts the years."

## 4.3 Present Value of a Single Sum

@! Go slowly here.
> The reverse question: how large a deposit today will reach a target later?
Now we turn the question round. The bakery's owner needs Tk 2,00,000 in five years to replace equipment. Instead of asking what a deposit will become, the owner asks: how large a deposit today will become Tk 2,00,000? This is a move to the *left* on the timeline. Begin with small numbers. If Tk 1,21,000 is wanted in two years, and the rate is 10%, we know from section 4.2 that Tk 1,00,000 grows to Tk 1,21,000. So the answer is Tk 1,00,000.

@ Discounting | Finding the present value of a later sum.
@ Discount rate | The yearly rate used to bring a later sum back to today. (In daily life, a discount is a cut in price.)
> Finding a present value is called discounting, and the rate used is the discount rate.
Finding a present value is called **discounting**, and the rate we use is called the **discount rate**. It is the same yearly rate as before. In section 4.2 we called it the interest rate, because it carried a sum forward. When the same rate brings a sum back to today, we call it the discount rate. It is one rate with two names, chosen by the direction of travel. In daily life a discount is a cut in price, and the two meanings are related: a later sum is priced below its face amount today.

> The rule for present value: divide by the multiplier that compounding would use.
Discounting is compounding run backwards. Where we multiplied, we now divide. The rule in words: the present value equals the future value divided by one plus the discount rate, raised to the power of the number of years. In symbols, PV = FV ÷ (1 + r)ⁿ. Dividing by a number is the same as multiplying by one divided by it, so we can write PV = FV × (1 + r)⁻ⁿ, the minus-sign power of section 3.2. The number (1 + r)⁻ⁿ is the multiplier that carries a sum n years back.

> First worked example of discounting, with clean numbers.
*Given.* FV = Tk 1,21,000 due in 2 years; r = 10% = 0.10. *Find.* PV. *Formula.* PV = FV ÷ (1 + r)ⁿ. *Steps.* First, 1 + 0.10 = 1.10. Second, 1.10² = 1.21. Third, PV = 1,21,000 ÷ 1.21 = Tk 1,00,000. *Answer.* The present value is Tk 1,00,000. *Check.* Carry it forward again with section 4.2: 1,00,000 × 1.21 = Tk 1,21,000, which is the sum we began with.

> Second worked example: the bakery's replacement fund.
*Given.* FV = Tk 2,00,000, needed in 5 years, so on 1 April 2031; r = 8% = 0.08; the deposit would be made on 1 April 2026. *Find.* PV. *Formula.* PV = FV ÷ (1 + r)ⁿ. *Steps.* First, 1.08⁵ = 1.469328 (section 3.2). Second, PV = 2,00,000 ÷ 1.469328 = Tk 1,36,116.64, which is Tk 1,36,117 to the nearest taka.

> The answer, a check, and what the answer means.
*Answer.* The owner must set aside Tk 1,36,117 today. *Check.* Carry the sum forward: 1,36,117 × 1.469328 = Tk 2,00,000.5, which is Tk 2,00,000 within the rounding. The result means that Tk 1,36,117 today and Tk 2,00,000 in five years are equal in value at 8%. The difference, Tk 63,883, is the interest that the deposit will earn.

> Fig. 6 shows how present value shrinks as time passes and as the rate rises.
:fig The present value of Tk 1 due at the end of the year shown, at three discount rates. | fig_ch4_discount.svg

> How to read the discount figure and what it shows.
To read Fig. 6, look along the bottom for the number of years until the sum is received, and up the left side for what Tk 1 is worth today. All three lines start at 1.00, because a sum received today is worth its full amount. Each line falls as the years increase. The line for 12% falls fastest. After ten years, Tk 1 is worth Tk 0.68 today at 4%, Tk 0.46 at 8%, and only Tk 0.32 at 12%.

> Third worked example: the opening puzzle is settled.
Now we can settle the second offer from the start of the chapter. *Given.* Take Tk 1,00,000 today, or Tk 1,10,000 in one year. *Find.* Which is worth more today at 8%, and at 12%. *Steps at 8%.* PV = 1,10,000 ÷ 1.08 = Tk 1,01,852. *Steps at 12%.* PV = 1,10,000 ÷ 1.12 = Tk 98,214. *Answer.* At 8% the later offer is worth Tk 1,852 more than Tk 1,00,000, so it is better to wait. At 12% it is worth Tk 1,786 less, so it is better to take the money today.

> Check, and the lesson: the answer depends on the discount rate.
*Check.* At 10%, PV = 1,10,000 ÷ 1.10 = Tk 1,00,000 exactly, so the two offers are equal. The owner who can earn only 8% should wait, and a person who can earn 12% elsewhere should take the money now. The lesson is important: the same two sums can rank in either order. The ranking depends on the discount rate, which is why the choice of rate matters so much in later chapters.

> Exceptions: the discount rate is not the same for everyone, and risk raises it.
Two exceptions need care. First, there is no single discount rate for the whole world. Each person or firm uses the rate it could earn elsewhere, or the rate it pays to borrow. Second, a risky promise should be discounted at a higher rate than a certain one, because risk lowers what a promise is worth today. We have assumed all payments certain. Chapters VIII to X teach how a higher rate is chosen when they are not.

> A sum at Year 0 is not discounted, because no time passes.
One small point on the timeline. A sum received at Year 0 has n = 0, and (1 + r)⁰ = 1. So its present value is the sum itself. Only sums that lie to the right of Year 0 are discounted. This will matter in Chapter V, where a stream of payments often begins with a sum today.

> Common slips in present value.
Four slips are common. First, multiplying by (1 + r)ⁿ instead of dividing. The answer then grows when it should shrink. Second, using the wrong number of years. Third, forgetting that a higher discount rate gives a *smaller* present value. Fourth, rounding the multiplier early, as in section 3.6. A quick check never fails: a present value must be smaller than the future value it comes from, if the rate is positive.

> Pause and check: the present value of Tk 90,000.
*Pause and check.* Find the present value of Tk 90,000 due in three years at a discount rate of 6%. State the given, the formula, the steps and a check. The answer is at the back of the book.

> You should now be able to say how a later sum is brought back.
*You should now be able to say:* "To bring a later sum to today, I divide it by 1 plus the discount rate, raised to the power of the number of years."

> A recap of the section.
*Before moving on.* Discounting is compounding backwards. The present value is FV ÷ (1 + r)ⁿ. The discount rate is the interest rate used in the backward direction. A higher rate or a longer time gives a smaller present value, and the same two sums can rank differently at different rates.

## 4.4 Rates, Periods and Compounding Frequency

> Interest may be added more often than once a year.
Until now interest was added once a year. Many banks add it more often: every six months, every quarter, or every month. The bank still states one *yearly* rate, such as 8%, but it adds a share of it at each shorter period. Because each addition begins to earn interest at once, more frequent addition gives a slightly larger sum. We need a rule that handles this, and the rule has two parts.

> The rule: divide the yearly rate by the number of periods in a year, and multiply the years by the same number.
Let m be the number of times in a year that interest is added. For half-yearly addition, m = 2. For quarterly, m = 4. For monthly, m = 12. Then the rate for each period is i = r ÷ m, and the number of periods is N = n × m. The earlier rule keeps its shape, with the new letters: FV = PV × (1 + i)^N, where N appears as the exponent. Always use i and N together, never r with N.

> First worked example: 8% for three years, added half-yearly.
*Given.* PV = Tk 1,00,000; r = 8% a year; n = 3 years; m = 2. *Find.* FV. *Formula.* i = r ÷ m, N = n × m, FV = PV × (1 + i)^N. *Steps.* First, i = 8% ÷ 2 = 4% = 0.04, and N = 3 × 2 = 6 periods. Second, 1.04² = 1.0816 and 1.04³ = 1.124864. Third, 1.04⁶ = 1.124864² = 1.265319. Fourth, FV = 1,00,000 × 1.265319 = Tk 1,26,531.90, which is Tk 1,26,532.

> The answer, a check, and the gain from the shorter period.
*Answer.* The future value is Tk 1,26,532. *Check.* This is slightly larger than Tk 1,25,971, the sum we found for yearly addition in section 4.2. The difference is Tk 561. Addition twice a year gave the interest of the first half-year a chance to earn interest in the second half. The table below shows the same 8% yearly rate with four ways of adding interest.

:table Tk 1,00,000 at 8% a year for three years, interest added at different intervals
| Interest added | Rate each period | Periods | Sum after 3 years (Tk) | Effective annual rate |
| Yearly | 8.00% | 3 | 1,25,971 | 8.00% |
| Half-yearly | 4.00% | 6 | 1,26,532 | 8.16% |
| Quarterly | 2.00% | 12 | 1,26,824 | 8.24% |
| Monthly | 0.67% | 36 | 1,27,024 | 8.30% |

@ Effective annual rate | The yearly rate that gives the same growth as the stated rate with interest added once a year.
> The effective annual rate tells us what a stated rate really earns in a year.
The last column of the table needs a new term. The **effective annual rate** means the yearly rate that gives the same growth when interest is added once a year. In symbols, effective annual rate = (1 + i)^m − 1. For half-yearly addition at 8%: 1.04² = 1.0816, so the effective annual rate is 0.0816, or 8.16%. A bank that states 8% and adds half-yearly really pays 8.16% a year. Always compare rates through the effective annual rate, when they are added at different intervals.

> Reading the table: more frequent addition gains, but with a limit.
Read down the table. Each shorter interval gives a larger sum, but the gains shrink. Moving from yearly to half-yearly adds Tk 561. Moving from half-yearly to quarterly adds only Tk 292. Moving from quarterly to monthly adds Tk 200. The effective rate rises from 8.00% to 8.30% but would never reach even 8.4%, however often interest is added. Frequency matters, but the stated rate matters far more.

> Second worked example: present value with quarterly addition.
*Given.* FV = Tk 2,00,000 due in 3 years; r = 12% a year added quarterly, so m = 4. *Find.* PV. *Formula.* PV = FV ÷ (1 + i)^N, with i = r ÷ m and N = n × m. *Steps.* First, i = 12% ÷ 4 = 3% = 0.03, and N = 3 × 4 = 12. Second, 1.03¹² = 1.425761. Third, PV = 2,00,000 ÷ 1.425761 = Tk 1,40,275.98, which is Tk 1,40,276.

> The answer, a check, and a comparison with yearly addition.
*Answer.* The present value is Tk 1,40,276. *Check.* Carry it forward: 1,40,276 × 1.425761 = Tk 2,00,000.0, as it should be. With yearly addition at 12%, the present value would be 2,00,000 ÷ 1.404928 = Tk 1,42,356. The quarterly case needs a *smaller* deposit, because the deposit grows faster when interest is added more often.

> Third worked example: an awkward period of eighteen months.
Periods need not be whole years. *Given.* PV = Tk 1,00,000 at 8% a year, added half-yearly, for 18 months. *Find.* FV. *Steps.* i = 4%, and N = 18 months ÷ 6 months = 3 periods. Then 1.04³ = 1.124864, so FV = 1,00,000 × 1.124864 = Tk 1,12,486. *Answer.* Tk 1,12,486. *Check.* The result lies between the sum after one year, Tk 1,08,160 (two half-years), and after two years, Tk 1,16,986 (four half-years), so it is sensible.

> Common slips with frequency.
Three slips are common. First, using the yearly rate with the number of periods: 8% for 6 periods is wrong; the rate must be 4%. Second, using the right rate and the wrong number of periods: three years of half-yearly addition is 6 periods, not 3. Third, forgetting to say how often interest is added. If the question gives no interval, assume it is added once a year.

> Pause and check: Tk 75,000 at 6%, added quarterly.
*Pause and check.* Find the future value of Tk 75,000 invested for two years at 6% a year, with interest added every quarter. The answer is at the back of the book.

> A recap of the section.
*Before moving on.* When interest is added m times a year, use i = r ÷ m and N = n × m. The effective annual rate, (1 + i)^m − 1, shows what the stated rate really earns. More frequent addition gives a larger sum, with gains that shrink. You should now be able to say: "I match the rate to the period before I raise it to a power."

## 4.5 Reading the Four Factor Tables

> Tables store the multipliers in advance, so that no power key is needed.
A power key makes our work quick, but not everyone has one at hand, and people prepared tables of multipliers long before calculators existed. A table stores the multiplier for each pair of rate and years. We find the multiplier and use it. Tables are still taught because they show patterns that a single calculator answer hides, and because a table lets us check a calculator result quickly.

@ Factor | A table number to multiply by. (In daily life, a cause or influence.)
> A factor is a table number that we multiply by.
In a table of this kind, each number is called a **factor**. A factor means a table number to multiply by. The factor for a sum moving forward is (1 + r)ⁿ, and the factor for a sum moving back is (1 + r)⁻ⁿ. Four tables are in common use. This chapter needs the first two. We preview the other two, which belong to Chapter V.

> Tables one and two are introduced in words before they are shown.
Table 1 gives the *future value factor of one taka*: what Tk 1 becomes after n years at rate r. Table 2 gives the *present value factor of one taka*: what Tk 1 due after n years is worth today. Each table has the years in rows and the rates in columns. Because the factors are for Tk 1, we multiply the factor by our own sum to find the answer.

:table Table 1. Future value factor of Tk 1 = (1 + r)ⁿ
| Years | 4% | 6% | 8% | 10% | 12% |
| 1 | 1.0400 | 1.0600 | 1.0800 | 1.1000 | 1.1200 |
| 2 | 1.0816 | 1.1236 | 1.1664 | 1.2100 | 1.2544 |
| 3 | 1.1249 | 1.1910 | 1.2597 | 1.3310 | 1.4049 |
| 4 | 1.1699 | 1.2625 | 1.3605 | 1.4641 | 1.5735 |
| 5 | 1.2167 | 1.3382 | 1.4693 | 1.6105 | 1.7623 |
| 6 | 1.2653 | 1.4185 | 1.5869 | 1.7716 | 1.9738 |
| 7 | 1.3159 | 1.5036 | 1.7138 | 1.9487 | 2.2107 |
| 8 | 1.3686 | 1.5938 | 1.8509 | 2.1436 | 2.4760 |
| 10 | 1.4802 | 1.7908 | 2.1589 | 2.5937 | 3.1058 |

:table Table 2. Present value factor of Tk 1 = (1 + r)⁻ⁿ
| Years | 4% | 6% | 8% | 10% | 12% |
| 1 | 0.9615 | 0.9434 | 0.9259 | 0.9091 | 0.8929 |
| 2 | 0.9246 | 0.8900 | 0.8573 | 0.8264 | 0.7972 |
| 3 | 0.8890 | 0.8396 | 0.7938 | 0.7513 | 0.7118 |
| 4 | 0.8548 | 0.7921 | 0.7350 | 0.6830 | 0.6355 |
| 5 | 0.8219 | 0.7473 | 0.6806 | 0.6209 | 0.5674 |
| 6 | 0.7903 | 0.7050 | 0.6302 | 0.5645 | 0.5066 |
| 7 | 0.7599 | 0.6651 | 0.5835 | 0.5132 | 0.4523 |
| 8 | 0.7307 | 0.6274 | 0.5403 | 0.4665 | 0.4039 |
| 10 | 0.6756 | 0.5584 | 0.4632 | 0.3855 | 0.3220 |

> To read a factor, find the row for the years and the column for the rate.
To read a factor, run one finger along the row for the number of years and another down the column for the rate, as we learned in section 3.3. Where they meet is the factor. In Table 1, the row for 5 years and the column for 8% meet at 1.4693. In Table 2, the same row and column meet at 0.6806. These are the two numbers we have already met by calculator in sections 4.2 and 4.3.

> The two tables are linked: each number in Table 2 is one divided by the matching number in Table 1.
The tables are not separate. Each factor in Table 2 equals one divided by the matching factor in Table 1. Check with 5 years at 8%: 1 ÷ 1.4693 = 0.6806. This is the same link as between compounding and discounting. It also means that a single table is enough, if we are ready to divide. The check is a quick way to see whether a number in a table has been copied wrongly.

> Using a table to find a future value, and why the answer differs slightly from the calculator's.
*Given.* Tk 1,00,000 at 8% for 3 years. *Find.* FV by the table. *Steps.* Table 1, row 3 and column 8%, gives 1.2597. Then 1,00,000 × 1.2597 = Tk 1,25,970. *Answer.* Tk 1,25,970. *Check.* The calculator gave Tk 1,25,971 in section 4.2. The gap of Tk 1 comes from the table's four decimals: 1.259712 was cut to 1.2597. In this book, answers use the calculator unless a question says to use the table, and a table answer may differ by a few taka.

> Using a table to find a present value.
*Given.* Tk 2,00,000 due in 5 years at 8%. *Find.* PV by the table. *Steps.* Table 2, row 5 and column 8%, gives 0.6806. Then 2,00,000 × 0.6806 = Tk 1,36,120. *Answer.* Tk 1,36,120. *Check.* The calculator gave Tk 1,36,117. The gap of Tk 3 is again the effect of four decimals. Both are close enough to show that the method is right.

> Using a table backwards to find the rate.
Tables also solve for an unknown rate or time. *Given.* Tk 80,000 grows to Tk 1,17,544 in 5 years. *Find.* The rate. *Steps.* The factor is 1,17,544 ÷ 80,000 = 1.4693. In Table 1, read along the row for 5 years until you find 1.4693. It sits under 8%. *Answer.* The rate is 8%. *Check.* 80,000 × 1.4693 = Tk 1,17,544, as given.

> Using a table backwards to find the years, with an estimate between two rows.
*Given.* Tk 50,000 is to double to Tk 1,00,000 at 10% a year. *Find.* The years. *Steps.* The factor is 2.0000. Look down the 10% column of Table 1. Row 7 shows 1.9487, which is below 2, and row 8 shows 2.1436, which is above 2. So the answer is between 7 and 8 years. A straight-line estimate gives 7 + (2.0000 − 1.9487) ÷ (2.1436 − 1.9487) = 7 + 0.0513 ÷ 0.1949 = 7.26 years. *Answer.* About 7.3 years. *Check.* The calculator method of section 4.2 gives 7.27 years.

> The limits of tables: only printed rates and years, and a straight-line estimate is only an estimate.
Tables have limits. They print only some rates and some years, so a rate such as 9.5% needs a calculator. The straight-line estimate between two rows is close, but not exact, because compounding follows a curve. A careful worker uses the table to see the pattern and the calculator for the exact answer.

> Tables three and four are previewed here, and used in Chapter V.
Two more tables complete the set. Table 3 gives the future value of Tk 1 paid at the end of *every* year for n years. Table 4 gives the present value of Tk 1 paid at the end of every year for n years. Chapter V teaches how to use them, with equal payments called annuities. The table below shows all four factors side by side at 8%, so that you can see how they relate.

:table The four tables at 8%, years 1 to 5
| Years | Table 1 | Table 2 | Table 3 | Table 4 |
| 1 | 1.0800 | 0.9259 | 1.0000 | 0.9259 |
| 2 | 1.1664 | 0.8573 | 2.0800 | 1.7833 |
| 3 | 1.2597 | 0.7938 | 3.2464 | 2.5771 |
| 4 | 1.3605 | 0.7350 | 4.5061 | 3.3121 |
| 5 | 1.4693 | 0.6806 | 5.8666 | 3.9927 |

> Reading the four-table comparison.
Read the table across. Tables 1 and 2 are for a single sum, and each Table 2 factor is one divided by the Table 1 factor in the same row. Tables 3 and 4 are for equal payments each year. The first row of Table 3 is 1.0000, because one payment at the end of year 1 has not yet earned anything. The second row is 1 + 1.08 = 2.08, which is the second payment plus the first payment grown by one year. Do not worry if this is not clear yet; Chapter V explains it.

> Pause and check: using the tables.
*Pause and check.* Use Table 1 to find the future value of Tk 2,00,000 invested for 5 years at 6%. Use Table 2 to find the present value of Tk 3,00,000 due in 4 years at 10%. The answers are at the back of the book.

> A recap of the section.
*Before moving on.* A factor is a table number to multiply by. Table 1 carries a sum forward and Table 2 brings it back, and each Table 2 factor is one divided by the Table 1 factor. A table answer can differ from a calculator answer by a few taka. You should now be able to say: "I can read a factor, and I can use a table to find a rate or the years."

## The Worked Case: The Spare Cash and the Replacement Fund

> The case file for April 2026, and the owner's three questions.
:case *Case file, illustrative.* Sundial Bakery, Dhaka. On 1 April 2026 the owner places Tk 1,00,000 of spare cash in a bank deposit at 8% a year, with interest added once a year. The equipment will need replacing in 5 years, on 1 April 2031, at an expected cost of Tk 2,00,000. The owner asks three questions: what the deposit will be worth on 1 April 2029; what sum must be set aside on 1 April 2026 to meet the replacement cost; and whether adding interest half-yearly would change the sum needed.

> The plan: two moves along the timeline and one change of period.
*Reasoning plan.* The first question moves a sum to the right on the timeline, so it asks for a future value. The second question moves a sum to the left, so it asks for a present value. The third question keeps the move to the left but changes the period from one year to half a year. We answer each in turn, with the standard layout of Given, Find, Formula, Steps, Answer and Check.

> Question one: the deposit on 1 April 2029.
*Given.* PV = Tk 1,00,000; r = 8%; n = 3 years. *Find.* FV. *Formula.* FV = PV × (1 + r)ⁿ. *Steps.* 1.08³ = 1.259712, and 1,00,000 × 1.259712 = Tk 1,25,971.20. *Answer.* Tk 1,25,971 on 1 April 2029. *Check.* Table 1, row 3 and column 8%, gives 1.2597, so the table answer is Tk 1,25,970, within one taka of the calculator.

> Question two: the sum to set aside today.
*Given.* FV = Tk 2,00,000; r = 8%; n = 5 years. *Find.* PV. *Formula.* PV = FV ÷ (1 + r)ⁿ. *Steps.* 1.08⁵ = 1.469328, and 2,00,000 ÷ 1.469328 = Tk 1,36,116.64. *Answer.* Tk 1,36,117. *Check.* Table 2, row 5 and column 8%, gives 0.6806. Then 2,00,000 × 0.6806 = Tk 1,36,120, within Tk 3 of the calculator answer.

> Question three: half-yearly addition lowers the sum needed.
*Given.* FV = Tk 2,00,000; r = 8% a year, added half-yearly; n = 5 years. *Find.* PV. *Formula.* PV = FV ÷ (1 + i)^N, with i = r ÷ 2 and N = n × 2. *Steps.* i = 4% and N = 10. Then 1.04¹⁰ = 1.480244, and 2,00,000 ÷ 1.480244 = Tk 1,35,112.83. *Answer.* Tk 1,35,113. *Check.* This is Tk 1,004 less than the yearly case, as it should be, because interest added twice a year makes a deposit grow faster.

> The conclusion: the spare cash is not yet enough, and two routes show the shortfall.
*Conclusion.* The spare cash of Tk 1,00,000 will be worth Tk 1,25,971 on 1 April 2029. To meet Tk 2,00,000 on 1 April 2031, the owner needs Tk 1,36,117 today with yearly interest, or Tk 1,35,113 with half-yearly interest. The Tk 1,00,000 is therefore short by Tk 36,117 today. The same gap can be seen at the end: Tk 1,00,000 would grow to Tk 1,46,933 in five years, which is Tk 53,067 short of Tk 2,00,000, and 53,067 ÷ 1.469328 = Tk 36,117. Chapter V shows how a plan of equal yearly deposits can reach the same goal.

## Summary

> A summary of the time value of money and the two moves.
A taka now is worth more than a taka later, mainly because money can earn interest. This is the time value of money. A timeline marks today as Year 0 and shows each sum at its date. Moving a sum to the right is compounding, and it gives a future value: FV = PV × (1 + r)ⁿ. Moving a sum to the left is discounting, and it gives a present value: PV = FV ÷ (1 + r)ⁿ. The same rate is used in both directions, and it is called the discount rate when it brings a sum back.

> A summary of frequency, tables and the cautions.
When interest is added m times a year, use the rate i = r ÷ m for N = n × m periods. The effective annual rate shows what a stated rate really earns. A factor is a table number to multiply by, and Tables 1 and 2 carry a sum forward and back. A higher rate or a longer time makes a present value smaller and a future value larger. All our sums were certain; risk comes in Chapter VIII.

## Think It Through

> An uncle's two offers, compared at two different discount rates.
An uncle wishes to help his niece. He offers her one of two gifts. Offer A is Tk 5,00,000 today. Offer B is Tk 3,00,000 today and a further Tk 2,50,000 in two years. First find the present value of Offer B at a discount rate of 10%, and say which offer is better. Then do the same at 20%. Finally explain, in two sentences, why the answer changed, and say what the niece should ask herself before choosing.

## Where People Go Wrong

> Mistake one: comparing sums at different dates without bringing them to one date.
*Comparing Tk 1,00,000 today with Tk 1,10,000 next year as if they were taken on the same day.* Sums at different dates cannot be compared until they are brought to the same date. Move them both to Year 0, or both to the same later year.

> Mistake two: using the percentage as a whole number in the formula.
*Writing 8 instead of 0.08.* A rate enters the formula as a decimal. With 8 in place of 0.08, the multiplier becomes 9 instead of 1.08, and the answer is absurd. Estimate first, as in section 3.6.

> Mistake three: multiplying by the number of years instead of using a power.
*Multiplying instead of raising to a power.* The future value after three years is PV × 1.08³, not PV × 1.08 × 3. The second gives 3.24, and the first gives 1.2597.

> Mistake four: multiplying when the question needs division, or the reverse.
*Multiplying when the sum lies in the future and we want today.* A present value must be smaller than the later sum it comes from. If your answer is larger, you have multiplied where you should divide.

> Mistake five: mismatching the rate and the period.
*Using the yearly rate with half-yearly periods.* If interest is added half-yearly, the rate in the formula is half the yearly rate, and the number of periods is twice the years.

> Mistake six: believing a higher discount rate raises present value.
*Thinking a higher discount rate gives a larger present value.* The opposite is true. A higher rate makes later sums worth less today, as Fig. 6 shows.

> Mistake seven: trusting a table answer to be exact.
*Expecting a table answer to match the calculator to the last taka.* Table factors have four decimals. A difference of a few taka is normal and does not mean the method is wrong.

## In History

> Fibonacci's book of 1202 taught Italian merchants the arithmetic of trade, which included interest.
In 1202, a man from Pisa, in what is now Italy, completed a book. His name was Leonardo of Pisa, and today he is better known as Fibonacci. As a boy he had lived in Africa, where he met the Hindu-Arabic figures that we use today. His book, *Liber Abaci*, or the *Book of Calculation*, taught these figures to Italian merchants. A second edition followed in 1228.^1

> The book's later problems came from trade, and included the price of goods, profit and interest.
The book did not stop at the figures. It gave merchants worked problems from their trade: the price of goods, the profit on a sale, the change of one currency into another, and the computation of interest. A merchant who lent money, or who waited for a payment, needed to know what a sum would become after a time. The idea of this chapter, that money has a value that changes with time, belongs to that long tradition of practical arithmetic.

> A short note on the person and his time, for readers unfamiliar with him.
For readers meeting him for the first time: Fibonacci lived in Pisa, a trading city, in the late twelfth and early thirteenth centuries. Merchants there traded with ports around the Mediterranean, and they needed methods that were quick and exact. His book gave them such methods. We carry the sums of this chapter on calculators now, but the questions are the questions of his merchants: how much will this grow, and what is that later sum worth today?

## Review Questions

> Question one: a future value with new data.
1. A firm places Tk 2,50,000 in a deposit at 6% a year, with interest added yearly. Find its value after 4 years. Show the given, the formula, the steps and a check.

> Question two: a present value with new data.
2. A firm will receive Tk 4,00,000 in 6 years. The discount rate is 12%. Find the present value. Show a check by carrying your answer forward.

> Question three: finding the rate.
3. Tk 40,000 grows to Tk 58,564 in 4 years. Find the yearly rate, and check your answer.

> Question four: finding the years by trial.
4. How many years does Tk 1,00,000 need to double at 12% a year? Use trial multiplication, and say between which two whole years the answer lies.

> Question five: compounding frequency.
5. Find the value of Tk 3,00,000 after 2 years at 12% a year, with interest added quarterly. Compare it with the value if interest is added yearly, and state the difference.

> Question six: the effective annual rate.
6. A bank states 12% a year, with interest added monthly. Find the effective annual rate.

> Question seven: a present value with half-yearly addition.
7. Tk 5,00,000 is due in 3 years. Interest is added half-yearly at 10% a year. Find the present value.

> Question eight: a goal case.
8. A school fund needs Tk 10,00,000 in 8 years. The discount rate is 9% a year, added yearly. How much must be set aside today? If only Tk 4,00,000 is available today, what extra sum is needed today?

> Question nine: using the tables.
9. Use Table 1 to find the future value of Tk 1,50,000 at 10% for 6 years. Use Table 2 to find the present value of Tk 2,00,000 due in 8 years at 12%.

> Question ten: explain in your own words.
10. In two or three sentences each, explain why a present value is smaller at 12% than at 8%, and why compound interest gives a larger sum than simple interest over a long time.

^1: Dates and the content of *Liber Abaci* are from standard histories of mathematics; see the verification note at the end of the chapter work.
