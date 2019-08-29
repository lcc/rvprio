# Case Study

## Datasets

- [Subjects](https://github.com/sallynathi/rvprio/blob/master/case-study/subjects.csv)
- [Dataset without prioritization](https://github.com/sallynathi/rvprio/blob/master/case-study/dataset.csv)
- [Dataset with prioritization](https://github.com/sallynathi/rvprio/blob/master/case-study/dataset_prioritized.csv)
- [Dataset with hierarchical prioritization](https://github.com/sallynathi/rvprio/blob/master/case-study/dataset_prioritized_hrchy.csv)
- [Results of manual inspection](https://github.com/sallynathi/rvprio/blob/master/case-study/manual_inspection.csv)

## Results

The following table shows the inspections done on the subjects **with prioritization**.
[CSV file for the following table](https://github.com/sallynathi/rvprio/blob/master/case-study/manual_inspection.csv)

The violated files are stored in [targets](https://github.com/sallynathi/rvprio/tree/master/case-study/targets) directory.

Conclusion Legend
- TrueBug: Might potentially cause bug under some cases
- FalseAlarm: Will never introduce any substantial problem
- Unknown: Should be discussed later
- Undefined: Cannot find source code, library or property description

| \#  | id  | Project Name              | SHA      | Filename:Line number                                                                                            | Specification                              | Severity   | Conclusion |
|-----|-----|---------------------------|----------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------|------------|------------|
| 1   | 209 | apache\.activemq\-artemis | e2d6d072 | org\.jboss\.shrinkwrap\.impl\.base\.MemoryMapArchiveBase\.java:398                                              | Collections\_SynchronizedMap               | error      | TrueBug    |
| 2   | 210 | apache\.activemq\-artemis | e2d6d072 | org\.jboss\.shrinkwrap\.impl\.base\.MemoryMapArchiveBase\.java:379                                              | Collections\_SynchronizedMap               | error      | TrueBug    |
| 3   | 129 | apache\.pdfbox            | 4c6428d7 | org\.apache\.fontbox\.ttf\.TTFSubsetter\.java:1134                                                              | TreeSet\_Comparable                        | error      | FalseAlarm |
| 4   | 130 | apache\.pdfbox            | 4c6428d7 | org\.apache\.fontbox\.ttf\.TTFSubsetter\.java:1134                                                              | SortedSet\_Comparable                      | error      | FalseAlarm |
| 5   | 99  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.test\.stax\.IVSplittingOutputStreamTest\.java:85                                    | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 6   | 100 | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.test\.stax\.IVSplittingOutputStreamTest\.java:86                                    | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 7   | 16  | apache\.juneau            | 0e0c0a0a | org\.apache\.juneau\.rest\.RestContext\.java:5237                                                               | Collections\_SynchronizedMap               | error      | Unknown    |
| 8   | 194 | apache\.activemq\-artemis | e2d6d072 | org\.apache\.activemq\.artemis\.core\.server\.group\.impl\.ClusteredResetMockTest\.java:112                     | CharSequence\_NotInSet                     | warning    | FalseAlarm |
| 9   | 147 | apache\.pdfbox            | 4c6428d7 | org\.apache\.pdfbox\.cos\.TestCOSStream\.java:158                                                               | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 10  | 249 | apache\.struts            | 570f8c3e | com\.opensymphony\.xwork2\.ognl\.OgnlValueStackFactory\.java:97                                                 | Map\_UnsafeIterator                        | error      | FalseAlarm |
| 11  | 18  | apache\.juneau            | 0e0c0a0a | org\.apache\.juneau\.rest\.mock2\.MockServletResponse\.java:346                                                 | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | FalseAlarm |
| 12  | 179 | apache\.stanbol           | 2fcf471b | org\.semanticweb\.owlapi\.vocab\.OWLRDFVocabulary\.java:393                                                     | CharSequence\_NotInSet                     | warning    | FalseAlarm |
| 13  | 182 | apache\.stanbol           | 2fcf471b | org\.semanticweb\.owlapi\.vocab\.OWLFacet\.java:90                                                              | CharSequence\_NotInSet                     | warning    | FalseAlarm |
| 14  | 97  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.test\.stax\.IVSplittingOutputStreamTest\.java:170                                   | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 15  | 98  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.test\.stax\.IVSplittingOutputStreamTest\.java:171                                   | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 16  | 101 | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.test\.stax\.IVSplittingOutputStreamTest\.java:114                                   | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 17  | 102 | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.test\.stax\.IVSplittingOutputStreamTest\.java:115                                   | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 18  | 204 | apache\.activemq\-artemis | e2d6d072 | org\.apache\.activemq\.artemis\.protocol\.amqp\.converter\.message\.JMSMappingOutboundTransformerTest\.java:582 | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 19  | 205 | apache\.activemq\-artemis | e2d6d072 | org\.apache\.activemq\.artemis\.protocol\.amqp\.converter\.message\.JMSMappingOutboundTransformerTest\.java:584 | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | FalseAlarm |
| 20  | 6   | apache\.juneau            | 0e0c0a0a | org\.apache\.juneau\.serializer\.OutputStreamSerializerSession\.java:87                                         | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | FalseAlarm |
| 21  | 29  | apache\.hive              | 333264b2 | org\.apache\.hive\.common\.util\.TestBloomFilter\.java:557                                                      | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 22  | 30  | apache\.hive              | 333264b2 | org\.apache\.hive\.common\.util\.TestBloomFilter\.java:561                                                      | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 23  | 31  | apache\.hive              | 333264b2 | org\.apache\.hive\.common\.util\.TestBloomFilter\.java:565                                                      | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 24  | 157 | apache\.shiro             | 010e4567 | org\.apache\.shiro\.io\.DefaultSerializer\.java:50                                                              | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 25  | 3   | apache\.juneau            | 0e0c0a0a | org\.apache\.juneau\.utils\.ASet\.java:63                                                                       | CharSequence\_NotInSet                     | warning    | FalseAlarm |
| 26  | 145 | apache\.pdfbox            | 4c6428d7 | org\.apache\.pdfbox\.filter\.ASCII85OutputStream\.java:238                                                      | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | FalseAlarm |
| 27  | 25  | apache\.juneau            | 0e0c0a0a | org\.apache\.juneau\.rest\.client\.RestRequestEntity\.java:87                                                   | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 28  | 93  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.test\.stax\.IVSplittingOutputStreamTest\.java:62                                    | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 29  | 94  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.test\.stax\.IVSplittingOutputStreamTest\.java:63                                    | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 30  | 95  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.test\.stax\.IVSplittingOutputStreamTest\.java:141                                   | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 31  | 96  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.test\.stax\.IVSplittingOutputStreamTest\.java:142                                   | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 32  | 59  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.jcp\.xml\.dsig\.internal\.dom\.DOMSignedInfo\.java:221                                             | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | FalseAlarm |
| 33  | 60  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.jcp\.xml\.dsig\.internal\.dom\.DOMSignedInfo\.java:223                                             | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | FalseAlarm |
| 34  | 61  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.jcp\.xml\.dsig\.internal\.dom\.DOMSignedInfo\.java:237                                             | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | FalseAlarm |
| 35  | 176 | apache\.stanbol           | 2fcf471b | org\.openrdf\.model\.impl\.TreeModel\.java:654                                                                  | TreeSet\_Comparable                        | error      | FalseAlarm |
| 36  | 177 | apache\.stanbol           | 2fcf471b | org\.openrdf\.model\.impl\.TreeModel\.java:654                                                                  | SortedSet\_Comparable                      | error      | FalseAlarm |
| 37  | 229 | apache\.activemq\-artemis | e2d6d072 | org\.apache\.activemq\.cli\.test\.TestActionContext\.java:44                                                    | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 38  | 274 | apache\.struts            | 570f8c3e | org\.testng\.reporters\.jq\.ChronologicalPanel\.java:44                                                         | Collections\_SynchronizedCollection        | error      | TrueBug    |
| 39  | 190 | apache\.activemq\-artemis | e2d6d072 | org\.apache\.activemq\.artemis\.reader\.MessageUtil\.java:157                                                   | CharSequence\_UndefinedHashCode            | warning    | FalseAlarm |
| 40  | 191 | apache\.activemq\-artemis | e2d6d072 | org\.apache\.activemq\.artemis\.reader\.MessageUtil\.java:159                                                   | CharSequence\_UndefinedHashCode            | warning    | FalseAlarm |
| 41  | 192 | apache\.activemq\-artemis | e2d6d072 | org\.apache\.activemq\.artemis\.reader\.MessageUtil\.java:161                                                   | CharSequence\_UndefinedHashCode            | warning    | FalseAlarm |
| 42  | 203 | apache\.activemq\-artemis | e2d6d072 | org\.apache\.activemq\.artemis\.reader\.MessageUtil\.java:163                                                   | CharSequence\_UndefinedHashCode            | warning    | FalseAlarm |
| 43  | 28  | apache\.hive              | 333264b2 | org\.apache\.hadoop\.hive\.common\.type\.TestHiveDecimal\.java:2720                                             | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 44  | 22  | apache\.juneau            | 0e0c0a0a | org\.apache\.juneau\.PropertyStoreBuilder\.java:704                                                             | SortedSet\_Comparable                      | error      | FalseAlarm |
| 45  | 14  | apache\.juneau            | 0e0c0a0a | org\.apache\.juneau\.PropertyStoreBuilder\.java:712                                                             | SortedSet\_Comparable                      | error      | FalseAlarm |
| 46  | 54  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.c14n\.implementations\.NameSpaceSymbTable\.java:86                                  | TreeSet\_Comparable                        | error      | FalseAlarm |
| 47  | 55  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.c14n\.implementations\.NameSpaceSymbTable\.java:86                                  | SortedSet\_Comparable                      | error      | FalseAlarm |
| 48  | 237 | apache\.struts            | 570f8c3e | ognl\.OgnlOps\.java:221                                                                                         | Long\_BadParsingArgs                       | warning    | FalseAlarm |
| 49  | 1   | apache\.juneau            | 0e0c0a0a | org\.apache\.juneau\.config\.Config\.java:1833                                                                  | Collections\_SynchronizedCollection        | error      | TrueBug    |
| 50  | 148 | apache\.pdfbox            | 4c6428d7 | org\.apache\.pdfbox\.tools\.TestExtractText\.java:51                                                            | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 51  | 2   | apache\.juneau            | 0e0c0a0a | org\.apache\.juneau\.parser\.ParserReader\.java:402                                                             | Reader\_ManipulateAfterClose               | error      | FalseAlarm |
| 52  | 128 | apache\.pdfbox            | 4c6428d7 | org\.apache\.fontbox\.ttf\.OpenTypeScript\.java:305                                                             | TreeMap\_Comparable                        | error      | FalseAlarm |
| 53  | 103 | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.signature\.Reference\.java:738                                                      | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | FalseAlarm |
| 54  | 141 | apache\.pdfbox            | 4c6428d7 | org\.apache\.pdfbox\.pdmodel\.graphics\.image\.CCITTFactory\.java:148                                           | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 55  | 222 | apache\.activemq\-artemis | e2d6d072 | org\.jboss\.weld\.event\.ObserverNotifier\.java:269                                                             | Object\_MonitorOwner                       | error      | FalseAlarm |
| 56  | 32  | apache\.hive              | 333264b2 | org\.apache\.hive\.common\.util\.TestBloomKFilter\.java:509                                                     | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 57  | 33  | apache\.hive              | 333264b2 | org\.apache\.hive\.common\.util\.TestBloomKFilter\.java:512                                                     | ByteArrayOutputStream\_FlushBeforeRetrieve | warning    | TrueBug    |
| 58  | 50  | apache\.tika              | 86325105 | org\.apache\.lucene\.index\.DocumentsWriterFlushControl\.java:537                                               | Collection\_UnsynchronizedAddAll           | error      | Unknown    |
| 59  | 51  | apache\.tika              | 86325105 | org\.apache\.lucene\.index\.DocumentsWriterFlushControl\.java:538                                               | Collection\_UnsynchronizedAddAll           | error      | Unknown    |
| 60  | 160 | apache\.shiro             | 010e4567 | org\.apache\.shiro\.web\.filter\.mgt\.SimpleNamedFilterList\.java:91                                            | Collection\_UnsynchronizedAddAll           | error      | Unknown    |
| 61  | 120 | apache\.pdfbox            | 4c6428d7 | org\.apache\.fontbox\.cff\.CharStringHandler\.java:47                                                           | Collection\_UnsynchronizedAddAll           | error      | Unknown    |
| 62  | 244 | apache\.struts            | 570f8c3e | ognl\.OgnlContext\.java:590                                                                                     | Map\_UnsafeIterator                        | error      | FalseAlarm |
| 63  | 236 | apache\.struts            | 570f8c3e | com\.opensymphony\.xwork2\.conversion\.impl\.DefaultTypeConverter\.java:215                                     | Long\_BadParsingArgs                       | warning    | FalseAlarm |
| 64  | 170 | apache\.stanbol           | 2fcf471b | org\.apache\.stanbol\.commons\.indexedgraph\.IndexedGraph\.java:207                                             | TreeSet\_Comparable                        | error      | FalseAlarm |
| 65  | 171 | apache\.stanbol           | 2fcf471b | org\.apache\.stanbol\.commons\.indexedgraph\.IndexedGraph\.java:207                                             | SortedSet\_Comparable                      | error      | FalseAlarm |
| 66  | 172 | apache\.stanbol           | 2fcf471b | org\.apache\.stanbol\.commons\.indexedgraph\.IndexedGraph\.java:208                                             | TreeSet\_Comparable                        | error      | FalseAlarm |
| 67  | 173 | apache\.stanbol           | 2fcf471b | org\.apache\.stanbol\.commons\.indexedgraph\.IndexedGraph\.java:208                                             | SortedSet\_Comparable                      | error      | FalseAlarm |
| 68  | 174 | apache\.stanbol           | 2fcf471b | org\.apache\.stanbol\.commons\.indexedgraph\.IndexedGraph\.java:209                                             | TreeSet\_Comparable                        | error      | FalseAlarm |
| 69  | 175 | apache\.stanbol           | 2fcf471b | org\.apache\.stanbol\.commons\.indexedgraph\.IndexedGraph\.java:209                                             | SortedSet\_Comparable                      | error      | FalseAlarm |
| 70  | 265 | apache\.struts            | 570f8c3e | org\.apache\.logging\.log4j\.util\.PropertiesUtil\.java:318                                                     | TreeSet\_Comparable                        | error      | FalseAlarm |
| 71  | 266 | apache\.struts            | 570f8c3e | org\.apache\.logging\.log4j\.util\.PropertiesUtil\.java:318                                                     | SortedSet\_Comparable                      | error      | FalseAlarm |
| 72  | 267 | apache\.struts            | 570f8c3e | org\.apache\.logging\.log4j\.util\.PropertiesUtil\.java:320                                                     | TreeSet\_Comparable                        | error      | FalseAlarm |
| 73  | 268 | apache\.struts            | 570f8c3e | org\.apache\.logging\.log4j\.util\.PropertiesUtil\.java:320                                                     | SortedSet\_Comparable                      | error      | FalseAlarm |
| 74  | 39  | apache\.tika              | 86325105 | org\.apache\.tika\.parser\.multiple\.AbstractMultipleParser\.java:163                                           | Collection\_UnsynchronizedAddAll           | error      | FalseAlarm |
| 75  | 166 | apache\.stanbol           | 2fcf471b | org\.apache\.clerezza\.rdf\.core\.access\.TcProviderMultiplexer\.java:70                                        | TreeSet\_Comparable                        | error      | FalseAlarm |
| 76  | 167 | apache\.stanbol           | 2fcf471b | org\.apache\.clerezza\.rdf\.core\.access\.TcProviderMultiplexer\.java:70                                        | SortedSet\_Comparable                      | error      | FalseAlarm |
| 77  | 234 | apache\.struts            | 570f8c3e | org\.assertj\.core\.internal\.TypeComparators\.java:105                                                         | TreeMap\_Comparable                        | error      | FalseAlarm |
| 78  | 254 | apache\.struts            | 570f8c3e | org\.apache\.struts2\.dispatcher\.DefaultStaticContentLoader\.java:301                                          | URLDecoder\_DecodeUTF8                     | warning    | FalseAlarm |
| 79  | 64  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.c14n\.implementations\.Canonicalizer20010315\.java:238                              | TreeSet\_Comparable                        | error      | FalseAlarm |
| 80  | 65  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.c14n\.implementations\.Canonicalizer20010315\.java:238                              | SortedSet\_Comparable                      | error      | FalseAlarm |
| 81  | 66  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.c14n\.implementations\.Canonicalizer20010315\.java:284                              | TreeSet\_Comparable                        | error      | FalseAlarm |
| 82  | 67  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.c14n\.implementations\.Canonicalizer20010315\.java:284                              | SortedSet\_Comparable                      | error      | FalseAlarm |
| 83  | 71  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.c14n\.implementations\.Canonicalizer20010315\.java:250                              | TreeSet\_Comparable                        | error      | FalseAlarm |
| 84  | 72  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.c14n\.implementations\.Canonicalizer20010315\.java:250                              | SortedSet\_Comparable                      | error      | FalseAlarm |
| 85  | 91  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.c14n\.implementations\.Canonicalizer20010315\.java:231                              | TreeSet\_Comparable                        | error      | FalseAlarm |
| 86  | 92  | apache\.santuario\-java   | 3f4f5f40 | org\.apache\.xml\.security\.c14n\.implementations\.Canonicalizer20010315\.java:231                              | SortedSet\_Comparable                      | error      | FalseAlarm |
| 87  | 4   | apache\.juneau            | 0e0c0a0a | org\.apache\.juneau\.dto\.swagger\.Swagger\.java:730                                                            | TreeMap\_Comparable                        | error      | FalseAlarm |
| 88  | 188 | apache\.activemq\-artemis | e2d6d072 | org\.apache\.activemq\.artemis\.selector\.strict\.SimpleCharStream\.java:131                                    | Reader\_ManipulateAfterClose               | error      | TrueBug    |
| 89  | 250 | apache\.struts            | 570f8c3e | freemarker\.core\.SimpleCharStream\.java:116                                                                    | Reader\_ManipulateAfterClose               | error      | TrueBug    |
| 90  | 136 | apache\.pdfbox            | 4c6428d7 | org\.apache\.pdfbox\.pdmodel\.graphics\.image\.SampledImageReader\.java:128                                     | Closeable\_MeaninglessClose                | suggestion | FalseAlarm |

## Summary
We obtained **278 warnings on 11 projects** and we inspected **90 violations with 29 TrueBugs**.

| Apache projects   | SHA      | Violations | Inspected | TrueBugs |
|-------------------|----------|------------|-----------|----------|
| santuario\-java   | 3f4f5f40 | 66         | 24        | 10       |
| activemq\-artemis | e2d6d072 | 46         | 12        | 5        |
| struts            | 570f8c3e | 45         | 12        | 2        |
| pdfbox            | 4c6428d7 | 31         | 9         | 3        |
| juneau            | 0e0c0a0a | 27         | 10        | 2        |
| stanbol           | 2fcf471b | 23         | 12        | 0        |
| tika              | 86325105 | 18         | 3         | 0        |
| ambari            | b0596110 | 8          | 0         | 0        |
| hive              | 333264b2 | 6          | 6         | 6        |
| shiro             | 010e4567 | 5          | 2         | 1        |
| ranger            | f80ee0e7 | 3          | 0         | 0        |

