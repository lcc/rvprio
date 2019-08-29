# Datasets

## Features Selection
The following table shows the importance of each features for our classifiers. [CSV file for the following table](https://github.com/sallynathi/rvprio/blob/master/data/features_selected.csv).

| Feature                                              | Importance            |
|------------------------------------------------------|-----------------------|
| TOKEN                                                | 0\.185292575549184    |
| SPEC\_is\_ByteArrayOutputStream\_FlushBeforeRetrieve | 0\.149816105202913    |
| NLOC                                                 | 0\.144107812063358    |
| CC                                                   | 0\.0935875220088725   |
| PARAM                                                | 0\.0683130506603481   |
| SEVERITY\_is\_warning                                | 0\.0410285214871991   |
| SPEC\_is\_Iterator\_HasNext                          | 0\.0320159672495362   |
| SEVERITY\_is\_suggestion                             | 0\.0310673201261425   |
| SPEC\_is\_Collections\_SynchronizedCollection        | 0\.0275767012622758   |
| CompareObjectsWithEquals                             | 0\.0272644568453833   |
| MissingBreakInSwitch                                 | 0\.0217062000677915   |
| SPEC\_is\_Long\_BadParsingArgs                       | 0\.0168471532010263   |
| SEVERITY\_is\_error                                  | 0\.0157579618755543   |
| EmptyCatchBlock                                      | 0\.0146888574756749   |
| JumbledIncrementer                                   | 0\.0134212659762669   |
| SEVERITY\_is\_na                                     | 0\.0119492771895148   |
| UseLocaleWithCaseConversions                         | 0\.00955414431273459  |
| MethodWithSameNameAsEnclosingClass                   | 0\.00945851205849885  |
| EmptyWhileStmt                                       | 0\.00823654100506909  |
| SPEC\_is\_StringTokenizer\_HasMoreElements           | 0\.00811194931554754  |
| UseCorrectExceptionLogging                           | 0\.00670923270208594  |
| SPEC\_is\_Collections\_SynchronizedMap               | 0\.00602768651589117  |
| DontImportSun                                        | 0\.00506203173649278  |
| SPEC\_is\_CharSequence\_UndefinedHashCode            | 0\.00504274985459101  |
| SuspiciousOctalEscape                                | 0\.00463403099189189  |
| SPEC\_is\_InputStream\_ManipulateAfterClose          | 0\.00426570842628624  |
| SPEC\_is\_URLConnection\_Connect                     | 0\.0039816692918827   |
| SuspiciousHashcodeMethodName                         | 0\.00374804916642922  |
| SPEC\_is\_Short\_BadParsingArgs                      | 0\.00345414606046949  |
| SPEC\_is\_Byte\_BadParsingArgs                       | 0\.00309901695108323  |
| CloseResource                                        | 0\.00284097563203721  |
| SPEC\_is\_FSM373                                     | 0\.00266777079026925  |
| SPEC\_is\_FSM162                                     | 0\.00235840571593418  |
| NonStaticInitializer                                 | 0\.00227751328405826  |
| SPEC\_is\_Reader\_ManipulateAfterClose               | 0\.00219304989085156  |
| CloneMethodMustImplementCloneable                    | 0\.00207019498210647  |
| SPEC\_is\_Closeable\_MultipleClose                   | 0\.00193911137953097  |
| SimpleDateFormatNeedsLocale                          | 0\.00158046660703023  |
| SPEC\_is\_ListIterator\_hasNextPrevious              | 0\.00144496162137322  |
| AssignmentInOperand                                  | 0\.00106553349128028  |
| SPEC\_is\_Closeable\_MeaninglessClose                | 0\.00105149970700232  |
| UnnecessaryCaseChange                                | 0\.00103707764245847  |
| SPEC\_is\_CharSequence\_NotInMap                     | 0\.000847719836927538 |
| InvalidSlf4jMessageFormat                            | 0\.000576955128134152 |
| SPEC\_is\_Comparable\_CompareToNull                  | 0\.000158389122868915 |
| SPEC\_is\_Map\_UnsafeIterator                        | 0\.000036509235922468 |
| MisplacedNullCheck                                   | 0\.000027649302219501 |

## Training phase
This dataset was used for training the classifiers to generate the model. The table contains **112 columns** and **1170 inputs**.
[CSV file for the Training dataset](https://github.com/sallynathi/rvprio/blob/master/data/training.csv).

