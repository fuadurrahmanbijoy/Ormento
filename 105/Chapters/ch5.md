:chapter V | Streams of Cash: Annuities and Mixed Streams
:mood Many payments, spread across the years, and one honest total.
:desc Chapter 4 taught us to move one sum through time. Most business money does not travel alone: rent, loan repayments, savings and sales arrive again and again. This chapter shows how to value a whole series of payments, equal or unequal, and how to find the regular saving that reaches a goal.

> The bakery needs a large sum in five years but cannot pay it today.

Sundial Bakery, in Dhaka, must replace some equipment in five years. The replacement will cost Tk 2,00,000. Chapter 4 told the owner what that future sum is worth today: Tk 1,36,117 placed at 8% a year would grow to Tk 2,00,000. The owner, however, does not hold Tk 1,36,117 in spare cash. She holds something different: a steady profit, from which she can save a smaller sum at the end of each year.

> Each yearly deposit grows for a different length of time.

Here lies the puzzle. The first deposit will earn interest for four years. The second will earn for three years, and the last will earn for none, because the goal date arrives on the day it is paid. Chapter 4 can value each deposit, but only one at a time. Five deposits need five calculations and one addition. A savings plan of twenty years would need twenty calculations. Is there a shorter road?

> Equal payments allow a shortcut; unequal payments need a patient sum.

There is, and it rests on one observation. When the payments are equal and regular, the same arithmetic repeats, and a single table number can do the repeating for us. When the payments are unequal, no such shortcut exists, but the method stays plain: treat every payment as a single sum from Chapter 4, and add the results. This chapter teaches both, and it closes by returning to the bakery's question.

## 5.1 Kinds of Cash Streams

> A stream is any series of payments that arrive over time.

@ Stream | A series of payments made or received over time.

Money rarely moves once and then stops. A tenant pays rent every month. A bank customer repays a loan every year. A shop receives sales every day. We give the name **stream** to any series of payments made or received over time. A stream of five yearly deposits of Tk 10,000 is a stream; so is a list of six monthly rent payments.

> A single sum is the smallest stream: one payment at one time.

Chapter 4 dealt with the simplest case, the single sum, which is one payment at one moment. We can now see it as a stream with only one member. Every longer stream is, in the end, a set of single sums placed at different moments on the timeline. This simple fact will carry us through the whole chapter.

> Streams differ in the size of the payments and in the gaps between them.

@ Annuity | Equal payments made at equal gaps of time.

Streams differ in two ways: the size of each payment and the length of the gap between payments. Suppose first that all the payments are equal and all the gaps are equal. We call such a stream an **annuity**. An annuity is a stream of equal payments made at equal gaps of time. A deposit of Tk 10,000 at the end of each year for three years is an annuity. So is a rent of Tk 15,000 paid every month for a year.

> The word annuity once meant yearly, but now covers any equal gap.

The word *annuity* comes from a Latin root meaning *year*, so beginners expect it to mean yearly payments only. Today it covers any equal gap: a month, a quarter or a year. In this chapter the gap is always one year, to keep the arithmetic clear. The ideas, however, work for months in the same way, as Chapter 4 showed for compounding.

> A mixed stream has payments of different sizes.

@ Mixed stream | A stream whose payments have different sizes.

Now suppose the payments are not equal. A **mixed stream** is a stream whose payments have different sizes. A catering contract that pays Tk 50,000 in the first year, Tk 60,000 in the second and Tk 40,000 in the third is a mixed stream. Most real investments produce mixed streams, because sales rise and fall from year to year. We shall meet them again in Chapters 6 and 7.

> An instalment is one of several regular payments that clear a debt.

@ Instalment | One of several regular payments that together repay a debt.

Business people also use the word **instalment**. An instalment is one of several regular part-payments that together repay a debt or buy something over time. Suppose a shop buys a refrigerator for Tk 60,000 and pays Tk 5,000 each month for twelve months. The twelve instalments form an annuity. A loan repaid in equal instalments is an annuity from the lender's point of view.

> Firms meet streams whenever they borrow, save, invest or sell.

Why should a firm care about streams? Because almost every large business decision creates one. A loan creates a stream of instalments. A new machine creates a stream of extra sales over its life. A savings plan creates a stream of deposits. To judge any of these decisions, the manager must give the whole stream a single value today. Without that value, a choice between two plans would rest on guesswork.

> A table sets the three kinds of stream side by side.

The table below compares the three kinds. Read each row from left to right: the first column names the kind, the next two describe the payments and the gaps, and the last gives an example.

:table Three kinds of cash stream
| Kind | Payments | Gaps | Example |
| Single sum | One payment | Not applicable | Tk 1,00,000 received once, in 3 years |
| Annuity | All equal | All equal | Tk 10,000 deposited each year for 3 years |
| Mixed stream | Not all equal | Equal in this book | Tk 50,000, then Tk 60,000, then Tk 40,000 |

> One unequal payment is enough to destroy an annuity.

Now consider an exception, which catches many students. A stream of Tk 10,000, Tk 10,000 and Tk 10,500 is *not* an annuity, although it is almost equal. One different payment makes it a mixed stream. In the same way, equal payments at unequal gaps do not form an annuity. Both conditions must hold: equal payments and equal gaps.

> Pause and check: classify each stream.

*Pause and check.* Classify each stream as a single sum, an annuity or a mixed stream. (a) Tk 8,000 received at the end of each month for a year. (b) Tk 20,000, Tk 30,000 and Tk 25,000 received at the ends of three years. (c) Tk 90,000 received once in two years. The answers are at the back of the book.

> Recap: three kinds of stream, and what separates them.

*Before moving on.* A stream is a series of payments over time. An annuity has equal payments at equal gaps. A mixed stream has unequal payments. A single sum is one payment. You should now be able to say, in your own words, why Tk 10,000, Tk 10,000, Tk 10,500 is a mixed stream.

## 5.2 Ordinary Annuity and Annuity Due

> Equal payments can still differ in when each period's payment is made.

@! Go slowly here.

Two people each pay Tk 10,000 a month. The first is a worker who receives a wage at the end of each month, after the work is done. The second is a tenant who pays rent at the start of each month, before living in the house. Both streams are annuities. Yet one payment comes at the end of its month and the other at the start. Does that small difference change the value? In finance it does, and so we must name the two cases.

@! Go slowly here.

> The two timings have two names: ordinary annuity and annuity due.

@ Ordinary annuity | An annuity whose payments come at the end of each period.

@ Annuity due | An annuity whose payments come at the start of each period.

An **ordinary annuity** is an annuity whose payments are made at the end of each period. An **annuity due** is an annuity whose payments are made at the start of each period. A period here means one gap, which is one year in this chapter. The wage in our example resembles an ordinary annuity. The rent resembles an annuity due.

> Reading the figure: arrows show when each payment arrives.

The figure below shows both kinds. Each line is a timeline running from left to right through time. A short tick mark is a moment, and an arrow pointing down is a payment of Tk 10,000 at that moment. In the upper timeline the payments arrive at the ends of years 1, 2 and 3. In the lower timeline they arrive today, at the end of year 1 and at the end of year 2. Every payment has moved one year earlier.

:fig Three yearly payments of Tk 10,000: ordinary annuity above, annuity due below. | ch5_fig1.svg

> The end of one year and the start of the next are one moment.

Many students find this step confusing, because the lower timeline says *end of year 1* while the description says *start of year 2*. These are the same moment: the instant one year finishes is the instant the next begins. So a payment at the start of year 2 sits at the same point as a payment at the end of year 1. Keep this fact in mind, and the figure becomes easy to read.

> An earlier payment earns more interest, or loses less to discounting.

Why does the timing change the value? A deposit made one year earlier earns one more year of interest, so a stream of early deposits grows to more. A receipt that arrives one year earlier is discounted for one year less, so its present value is higher. In both cases, earlier means worth more. An annuity due is therefore always worth more than the ordinary annuity with the same payments, at any positive discount rate.

> A second bridge: a loan repaid at the end of each year.

Here is a second everyday bridge. A trader borrows money and promises to repay at the end of each year. The bank receives its money after the year has passed, so the repayments form an ordinary annuity. Compare a shop that sells goods on a plan requiring the first payment on the day of purchase. That plan resembles an annuity due. In each case, the only question to ask is: does the first payment come at the end of the first period, or at its start?

> When a problem is silent, we treat the payments as ordinary.

A rule of the book: unless a problem states otherwise, an annuity is an ordinary annuity, with each payment at the end of its year. Problems that intend the other case will say *at the start of each year*, or will describe a payment made today. Always search the wording for these clues before you begin.

> Pause and check: ordinary or due?

*Pause and check.* A school pays its teacher at the end of each month. Is that stream an ordinary annuity or an annuity due? A shopkeeper pays rent on the first day of each month. Which kind is the rent? The answers are at the back of the book.

> Recap: the two timings and why they matter.

*Before moving on.* Ordinary means end of period; due means start of period. Due is worth more, because each payment is one year earlier. You should now be able to say why a payment on the first day of a year is the same moment as a payment on the last day of the year before.

## 5.3 Future and Present Value of Annuities

> The first method treats each payment as a single sum from Chapter 4.

We begin with the method we already own. To value a stream, treat each payment as a single sum, value each one, and add. We shall do this once, slowly, for a small annuity. Then we shall see how a table number replaces the repeated work. Throughout this section, *i* is the discount rate written as a decimal, so that 10% is 0.10, and *n* is the number of years.

> The future value of an annuity is the sum of what each payment grows to.

The future value of an annuity is what all its payments are worth at the end of the last year, when each payment has earned interest from the day it was paid. Suppose Tk 10,000 is deposited at the end of each of three years, and the discount rate is 10%. The table below grows each deposit to the end of year 3.

:table Growing three deposits of Tk 10,000 at 10% to the end of year 3
| Deposit | Made at | Years of growth | Growth factor | Value at end of year 3 (Tk) |
| First | End of year 1 | 2 | 1.2100 | 12,100 |
| Second | End of year 2 | 1 | 1.1000 | 11,000 |
| Third | End of year 3 | 0 | 1.0000 | 10,000 |
| Total | | | 3.3100 | 33,100 |

> Add the growth factors once, and the result serves every deposit.

Look at the last row. The three growth factors add to 3.3100, and the three values add to Tk 33,100. Because every deposit is the same Tk 10,000, we may add the factors first and multiply once: Tk 10,000 × 3.3100 = Tk 33,100. The number 3.3100 depends only on the discount rate and the number of years. It does not depend on the size of the deposit.

> The annuity factor is the table number that serves a whole annuity.

@ Annuity factor | A table number that, times the payment, gives an annuity's value.

We call such a number an **annuity factor**. It is a table number that, multiplied by the regular payment, gives the value of the whole annuity. There are two: the *future value annuity factor*, which gives the future value, and the *present value annuity factor*, which gives the present value. In words, the rule for the future value is simple:

:box IN SHORT
Future value of an annuity = regular payment × future value annuity factor. In symbols, FVA = PMT × FVAF. Here FVA is the future value of the annuity, PMT is the regular payment, and FVAF is the future value annuity factor for the given discount rate and number of years.

> Where the factor comes from: a short formula, or the table.

The factor can be found from the tables of Chapter 4, or from a short formula. In words: take 1 plus the discount rate, raise it to the power *n*, subtract 1, and divide by the discount rate. In symbols, FVAF = [(1 + i) to the power n − 1] ÷ i. For i = 0.10 and n = 3, the power is 1.10 to the power 3, which is 1.3310, so FVAF = (1.3310 − 1) ÷ 0.10 = 3.3100. This matches the sum of the growth factors above, as it should.

> Worked example 5.1 lays out the future value in six steps.

Now the same calculation in the standard layout. Study each row; every example in this chapter follows the same order.

:table Worked example 5.1: future value of an ordinary annuity
| Step | Working |
| Given | Deposit Tk 10,000 at the end of each year; 3 years; discount rate 10% |
| Find | The value of the deposits at the end of year 3 |
| Formula | FVA = PMT × FVAF |
| Step 1 | FVAF for 10% and 3 years = 3.3100 |
| Step 2 | FVA = Tk 10,000 × 3.3100 |
| Answer | Tk 33,100 |
| Check | Deposits total only Tk 30,000, so Tk 33,100 is plausible; the extra Tk 3,100 is interest. The table above also gave Tk 33,100 |

> The present value of an annuity is the sum of what each payment is worth today.

The present value of an annuity is what all its payments are worth today, when each payment is discounted back to the present. The method mirrors the one above. We discount each payment with the factors of Chapter 4 and add. For the same three payments of Tk 10,000 at 10%, the payments are worth Tk 9,091, Tk 8,264 and Tk 7,513 today, which total Tk 24,868.

> The same shortcut works: add the factors once and multiply once.

The three discount factors are 0.9091, 0.8264 and 0.7513, which add to 2.4868. The table gives 2.4869, because its factor is calculated exactly and then rounded once, whereas our sum rounds three times. This tiny gap of one taka is a rounding effect, not an error. In words: present value of an annuity = regular payment × present value annuity factor. In symbols, PVA = PMT × PVAF. The factor can be found from [1 − 1 ÷ (1 + i) to the power n] ÷ i.

:table Worked example 5.2: present value of an ordinary annuity
| Step | Working |
| Given | Receive Tk 10,000 at the end of each year; 3 years; discount rate 10% |
| Find | The value today of the three receipts |
| Formula | PVA = PMT × PVAF |
| Step 1 | PVAF for 10% and 3 years = 2.4869 |
| Step 2 | PVA = Tk 10,000 × 2.4869 |
| Answer | About Tk 24,869 |
| Check | The receipts total Tk 30,000, and today's value must be smaller: Tk 24,869 is smaller. Also, Tk 24,869 × 1.3310 = Tk 33,100, the future value of Example 5.1 |

> A second, less tidy example uses an 8% rate and five years.

The first two examples used round numbers, so that the method stood alone. Real figures are less tidy. The next example uses 8% and five years, with a payment of Tk 18,000. The factors come from the table that follows this example, which gives 5.8666 for the future value and 3.9927 for the present value. Notice that the answers are not round, and that rounding to the nearest taka is sensible.

:table Worked example 5.3: both values of a less tidy annuity
| Step | Working |
| Given | A café receives Tk 18,000 at the end of each year; 5 years; discount rate 8% |
| Find | (a) the present value today; (b) the value at the end of year 5 |
| Formula | PVA = PMT × PVAF; FVA = PMT × FVAF |
| Step 1 | PVAF = 3.9927 and FVAF = 5.8666 for 8% and 5 years |
| Step 2 | PVA = Tk 18,000 × 3.9927 = Tk 71,869 |
| Step 3 | FVA = Tk 18,000 × 5.8666 = Tk 1,05,599 |
| Answer | Present value Tk 71,869; value at end of year 5 Tk 1,05,599 |
| Check | The receipts total Tk 90,000. The present value is below that total, and the year-5 value is above it, as discounting and growth require. Also Tk 71,869 × 1.4693 = Tk 1,05,599 |

> The tables below give annuity factors at 8% for the bakery's case.

The next table gives both annuity factors at 8% for one to five years, the rate used in the bakery's case. To read a row, find the number of years, then choose the column you need. For three years, 3.2464 means that three yearly deposits of Tk 1 grow to Tk 3.2464 at the end of year 3. The value 2.5771 means that three yearly receipts of Tk 1 are worth Tk 2.5771 today.

:table Annuity factors at a discount rate of 8%
| Years | Future value annuity factor | Present value annuity factor |
| 1 | 1.0000 | 0.9259 |
| 2 | 2.0800 | 1.7833 |
| 3 | 3.2464 | 2.5771 |
| 4 | 4.5061 | 3.3121 |
| 5 | 5.8666 | 3.9927 |

> An annuity due is the ordinary annuity multiplied by one plus the rate.

Now the annuity due. Every payment arrives one year earlier, so every payment earns one more year of interest, or is discounted one year less. This is the same as multiplying the ordinary answer once by (1 + i). The rule: value of an annuity due = value of the ordinary annuity × (1 + i). It holds for both future and present values.

:table Worked example 5.4: future value of an annuity due
| Step | Working |
| Given | Deposit Tk 10,000 at the start of each year; 3 years; discount rate 10% |
| Find | The value of the deposits at the end of year 3 |
| Formula | FVA due = FVA ordinary × (1 + i) |
| Step 1 | FVA ordinary = Tk 33,100 (Example 5.1) |
| Step 2 | FVA due = Tk 33,100 × 1.10 |
| Answer | Tk 36,410 |
| Check | Grow each deposit separately: Tk 13,310 + Tk 12,100 + Tk 11,000 = Tk 36,410 |

> The present value of the same due stream is also higher.

The present value follows the same logic. If the three payments of Tk 10,000 begin today, they are worth Tk 10,000 + Tk 9,091 + Tk 8,264 = Tk 27,355, which is larger than the Tk 24,869 of the ordinary case. The first payment is not discounted at all, because it is already in the present.

> Four slips cause most wrong answers in this section.

Beware of four common slips. The first is to use the future value factor when the problem asks for the present value, or the reverse. The second is to count the years wrongly: for three deposits, n is 3, not 2 or 4. The third is to mix months and years, using a yearly rate with monthly payments. The fourth is to forget that a table factor serves a payment of Tk 1, so it must be multiplied by the actual payment.

> Pause and check: a small annuity at 10%.

*Pause and check.* Using the method of Example 5.1, find the future value of Tk 5,000 deposited at the end of each of two years at 10%. Then find the future value if the deposits are made at the start of each year. The answers are at the back of the book.

> Recap: annuity value equals payment times factor.

*Before moving on.* Value of an annuity = payment × annuity factor. The factor depends on the rate and the years, not on the payment. For an annuity due, multiply the ordinary value by (1 + i). You should now be able to say why a factor of 3.3100 serves any size of payment.

## 5.4 Finding the Regular Payment for a Goal

> The same formula, turned around, gives the payment that reaches a target.

Until now the payment was known and the value was unknown. Often the position is reversed: the goal is known and the payment is unknown. The bakery's owner knows the goal, Tk 2,00,000 in five years. She needs the yearly deposit. Because FVA = PMT × FVAF, we divide both sides by the factor, and the rule becomes: payment = goal ÷ future value annuity factor.

> A sinking fund payment is the regular saving that reaches a target.

@ Sinking fund payment | A regular saving that reaches a target sum.

A **sinking fund payment** is a regular saving made to reach a target sum on a fixed date. The old name *sinking fund* describes a fund that grows by regular deposits until it can pay a large cost, such as replacing a machine. In symbols, PMT = FVA ÷ FVAF.

:table Worked example 5.5: the bakery's yearly deposit
| Step | Working |
| Given | Goal Tk 2,00,000 in 5 years; deposits at the end of each year; discount rate 8% |
| Find | The yearly deposit |
| Formula | PMT = FVA ÷ FVAF |
| Step 1 | FVAF for 8% and 5 years = 5.8666 (table above) |
| Step 2 | PMT = Tk 2,00,000 ÷ 5.8666 |
| Answer | Tk 34,091 a year |
| Check | Grow each deposit to the end of year 5, as in the figure below: Tk 46,381 + 42,945 + 39,764 + 36,819 + 34,091 = Tk 2,00,000 |

> Reading the figure: each deposit has a different amount of growth.

The figure below is the check in a picture. It is one tall column, built from five blocks, one for each deposit, with the total at the top. Each block shows what one deposit has become by the end of year 5. The first deposit, which was in the account for four years, has grown most. The last deposit has not grown at all, because it was paid on the goal date.

:fig Each yearly deposit of Tk 34,091 at 8%, valued at the end of year 5. | ch5_fig2.svg

> The deposits total less than the goal; interest supplies the rest.

Compare this with Chapter 4. A single sum of Tk 1,36,117 placed today would reach the goal. The owner chooses instead five deposits of Tk 34,091, which total Tk 1,70,455. The interest supplies the other Tk 29,545. She pays the cost gradually, from yearly profit, and the account earns the rest.

> If deposits are made at the start of each year, the payment falls.

Suppose, instead, she deposits at the start of each year. Each deposit then earns one more year, so the yearly deposit can be smaller. The annuity due factor is 5.8666 × 1.08 = 6.3359, and the payment is Tk 2,00,000 ÷ 6.3359 = Tk 31,566. The saving is Tk 2,525 a year, which is the reward for paying one year earlier.

> The present value factor gives the instalment that repays a loan.

The reverse idea works for loans. A lender gives a sum today, and the borrower repays it in equal instalments. The sum borrowed is the present value of the instalments. So instalment = amount borrowed ÷ present value annuity factor. Example 5.6 shows this for a small loan.

:table Worked example 5.6: the instalment that repays a loan
| Step | Working |
| Given | Borrow Tk 1,00,000 today; repay in 4 equal instalments at the end of each year; discount rate 10% |
| Find | The yearly instalment |
| Formula | PMT = PVA ÷ PVAF |
| Step 1 | PVAF for 10% and 4 years = 3.1699 |
| Step 2 | PMT = Tk 1,00,000 ÷ 3.1699 |
| Answer | Tk 31,547 a year |
| Check | Four instalments total Tk 1,26,188, which is more than Tk 1,00,000, as it should be, because interest is paid. Also Tk 31,547 × 3.1699 = Tk 1,00,000 |

> Common slips: dividing by the wrong factor, and mixing the timing.

Two slips are frequent here. A student may divide by the present value factor when saving for a goal, which gives the wrong answer; a goal in the future needs the *future* value factor. Another slip is to use the ordinary factor when the problem says *at the start of each year*. Choose the factor by asking two questions: is the known sum in the future or today, and do payments come at the end or the start?

> Pause and check: a goal and a loan.

*Pause and check.* A trader wants Tk 1,00,000 in three years and saves at the end of each year at 8%. The future value annuity factor for three years is 3.2464. Find the yearly saving. Then decide whether the same trader, paying at the start of each year, would save more or less each year, and why. The answers are at the back of the book.

## 5.5 Mixed Streams and Comparing Streams

> Two contracts pay the same total in different orders: are they equal?

A caterer offers the bakery two contracts. Each pays four yearly receipts, and each pays Tk 2,20,000 in total. The only difference is the order of the payments. Is one contract worth more than the other? Our understanding of time says yes, since earlier money is worth more. This section shows how to measure the difference in taka.

> A mixed stream has no shortcut; value each payment and add.

When payments are unequal, no single annuity factor exists. The method of Chapter 4 remains, and it is complete. Find the present value of each payment with its own discount factor, then add the present values. The sum is the present value of the stream. A stream's future value is found in the same way by growing each payment and adding.

> Example 5.7 discounts each receipt separately, then adds.

We now value Contract A, the bakery's own four-year catering contract, one receipt at a time. The table gives the factors, the present values and the total.^1

^1: The factors in the table are rounded to four places. The present values are calculated with the more exact factors of a calculator. The four rounded present values add to Tk 1,80,941; the exact total is Tk 1,80,942.

:table Worked example 5.7: present value of the bakery's catering receipts (Contract A)
| Step | Working |
| Given | Receipts at the end of years 1 to 4: Tk 50,000; Tk 60,000; Tk 40,000; Tk 70,000; discount rate 8% |
| Find | The present value of the stream |
| Formula | PV of stream = sum of (each receipt × its present value factor) |
| Step 1 | Factors at 8%: 0.9259 (year 1), 0.8573 (year 2), 0.7938 (year 3), 0.7350 (year 4) |
| Step 2 | Present values: Tk 46,296; Tk 51,440; Tk 31,753; Tk 51,452 |
| Step 3 | Add the four present values |
| Answer | Tk 1,80,942 |
| Check | The receipts total Tk 2,20,000, and the present value, Tk 1,80,942, is lower, as it must be. Each present value is below its own receipt |

> Reading the figure: each receipt has a shorter twin, its present value.

The figure below shows the same result as a picture. For each year there are two bars. The plain bar is the receipt, and the shaded bar beside it is its present value at 8%. The shaded bar is always shorter, and the gap grows as the year grows, because later money loses more value.

:fig The bakery's catering receipts and their present values at 8%. | ch5_fig3.svg

> Contract B pays the same sums in a different order.

Now Contract B. It pays Tk 70,000, Tk 50,000, Tk 60,000 and Tk 40,000 at the ends of years 1 to 4. The four payments are the same sums as Contract A, with the largest one moved to the first year. The table below sets both contracts side by side, using the same four discount factors.

:table Present values of two contracts at a discount rate of 8%
| Year | Factor | A: receipt (Tk) | A: present value (Tk) | B: receipt (Tk) | B: present value (Tk) |
| 1 | 0.9259 | 50,000 | 46,296 | 70,000 | 64,815 |
| 2 | 0.8573 | 60,000 | 51,440 | 50,000 | 42,867 |
| 3 | 0.7938 | 40,000 | 31,753 | 60,000 | 47,630 |
| 4 | 0.7350 | 70,000 | 51,452 | 40,000 | 29,401 |
| Total | | 2,20,000 | 1,80,942 | 2,20,000 | 1,84,713 |

> Contract B is worth Tk 3,771 more, though the totals are equal.

Both contracts pay Tk 2,20,000, yet Contract B is worth Tk 1,84,713 today and Contract A is worth Tk 1,80,942. The difference is Tk 3,771. Contract B delivers its large payment early, when it loses least value. This is the lesson of the whole book so far: *compare streams by their present values, at the same discount rate and on the same date, never by their totals*.

> A higher discount rate rewards early payments even more.

One exception deserves a note. The ranking of two streams can change if the discount rate changes. A higher rate lowers distant payments by more, so the stream with early payments gains. A stream that wins at 4% may lose at 15%. For this reason, a comparison must always name the rate it used.

> Pause and check: which stream is worth more?

*Pause and check.* Stream P pays Tk 10,000 at the end of year 1 and Tk 50,000 at the end of year 2. Stream Q pays Tk 50,000 at the end of year 1 and Tk 10,000 at the end of year 2. Both total Tk 60,000. Without calculating, which is worth more at any positive discount rate, and why? The answers are at the back of the book.

> Recap: how to value and compare a mixed stream.

*Before moving on.* A mixed stream is valued by discounting each payment and adding. Two streams are compared by present value at the same rate. You should now be able to say why the order of the payments matters when the total does not change.

## 5.6 Perpetuity in Brief

> A perpetuity is an annuity that never ends.

@ Perpetuity | An annuity that never ends.

A **perpetuity** is an annuity that never ends. Its payments continue for ever. At first this seems to give an infinite value, but later payments are discounted so heavily that the total stays finite. The present value is the payment divided by the discount rate: PV = PMT ÷ i. A payment of Tk 5,000 every year for ever, at 8%, is worth Tk 5,000 ÷ 0.08 = Tk 62,500 today. Check: Tk 62,500 earning 8% gives Tk 5,000 each year. We shall use this idea again in Chapter 11.

> A perpetuity is an idealisation, but a useful one.

No real payment continues for ever, so a perpetuity is an idealisation. Even so, it helps when payments last for a very long time, because distant payments have almost no present value. The perpetuity formula then gives a good estimate with one division. Its main use for us will come in Chapter 11, where we value a share that is expected to pay a steady dividend for many years.

* * *

> The case file applies both methods to one business.

:case Case file, illustrative. *Situation.* Sundial Bakery, Dhaka, must replace equipment costing Tk 2,00,000 in five years (Chapter 4). The owner will make five equal deposits, one at the end of each year, into an account paying 8% a year. Separately, a caterer offers two four-year contracts. Contract A pays Tk 50,000, Tk 60,000, Tk 40,000 and Tk 70,000 at the ends of years 1 to 4. Contract B pays Tk 70,000, Tk 50,000, Tk 60,000 and Tk 40,000.

> The question has two parts: a deposit and a comparison.

:case *Question.* What yearly deposit reaches Tk 2,00,000 in five years? Which contract is worth more today at 8%?

> The reasoning chooses the factor by the kind of stream.

:case *Reasoning.* The deposits are equal and regular, so they form an ordinary annuity with a known future value. We divide the goal by the future value annuity factor for 8% and five years. The catering receipts are mixed streams, so we discount each receipt and add.

> The conclusion gives both answers in taka.

:case *Conclusion.* The deposit is Tk 2,00,000 ÷ 5.8666 = Tk 34,091 a year. Contract A is worth Tk 1,80,942 today. Contract B is worth Tk 1,84,713 today, which is Tk 3,771 more, although each contract pays Tk 2,20,000 in total.

> The checks show both answers are sensible.

:case *Check.* Growing each deposit to year 5 gives Tk 2,00,000 in total (see the figure in section 5.4). Each contract's present value is below Tk 2,20,000, as discounting requires. The earlier-paying contract has the higher present value, as the theory predicts.

## Summary

> The summary restates the chapter's four ideas.

A stream is a series of payments over time. An annuity has equal payments at equal gaps; a mixed stream does not. An ordinary annuity pays at the end of each period, and an annuity due pays at the start, so the due is worth more by the factor (1 + i). The value of an annuity is the payment times an annuity factor, and the payment for a goal is the goal divided by the factor. A mixed stream is valued by discounting each payment and adding. Streams are compared by present value, never by total. A perpetuity is worth its payment divided by the discount rate.

## Think It Through

> Apply the methods to a new school canteen case.

A school canteen will need Tk 5,00,000 in four years to build a new kitchen. The canteen can earn 10% a year. (a) Find the yearly deposit, made at the end of each year, that reaches the goal. The future value annuity factor for 10% and four years is 4.6410. (b) Find the yearly deposit if payments are made at the start of each year. (c) Explain, in two sentences, why the second answer is smaller. The answers are at the back of the book.

## Where People Go Wrong

> Error one: adding payments without discounting them.

*Adding the payments as if time did not matter.* A stream of Tk 10,000 for five years is not worth Tk 50,000 today. Each payment is discounted, so the total present value is smaller. Correction: always multiply by a factor, or discount each payment.

> Error two: using the wrong table.

*Using the wrong factor.* The future value annuity factor answers *what will my deposits become?* The present value annuity factor answers *what are my receipts worth today?* Correction: ask first whether the known figure sits in the future or in the present.

> Error three: forgetting the timing of the payments.

*Ignoring the timing.* Payments at the start of each year are not payments at the end. Correction: look for words such as *start*, *beginning*, *today* or *in advance*, which signal an annuity due, and multiply the ordinary answer by (1 + i).

> Error four: calling a nearly equal stream an annuity.

*Calling an uneven stream an annuity.* A single different payment breaks the annuity. Correction: use the annuity factor only when every payment is equal and every gap is equal. Otherwise, discount each payment separately.

## In History

> A seventeenth-century state priced annuities by the methods of this chapter.

In the seventeenth century, several European governments raised money by selling life annuities. A life annuity pays a fixed sum each year for as long as the buyer lives. The price had to be fair: too low, and the state lost; too high, and no one bought. In 1671 Johan de Witt, a leading statesman of the Dutch Republic, wrote a report on the fair price of such annuities. He treated each yearly payment as a sum to be discounted, weighted by the chance that the buyer would still be alive. His method is a close relative of the present-value method of this chapter.

## Review Questions

> Review questions close the chapter.

:table Review questions for Chapter V
| No. | Question |
| 1 | Define an annuity. State two ways in which a stream can fail to be an annuity. |
| 2 | Explain the difference between an ordinary annuity and an annuity due. Which has the higher future value, and why? |
| 3 | Tk 20,000 is deposited at the end of each year for four years at 10%. Find the future value. (FVAF = 4.6410) |
| 4 | Find the future value if the deposits in question 3 are made at the start of each year. |
| 5 | Find the present value of Tk 25,000 received at the end of each year for five years at 8%. |
| 6 | A loan of Tk 2,00,000 is repaid in three equal year-end instalments at 8%. Find each instalment. |
| 7 | Stream X pays Tk 30,000, Tk 30,000 and Tk 90,000 at the ends of years 1 to 3. Stream Y pays Tk 90,000, Tk 30,000 and Tk 30,000. At 10%, which is worth more today, and by how much? |
| 8 | A perpetuity pays Tk 12,000 a year. Find its present value at 6%. |
| 9 | Explain why two streams with the same total can have different present values. |
