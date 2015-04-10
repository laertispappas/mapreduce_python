echo `hadoop fs -rm /user/hduser/tfidf/3-word-freq-in-corpus/*`
echo `hadoop fs -rmdir /user/hduser/tfidf/3-word-freq-in-corpus`

echo `hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper job3/mapper.py -reducer job3/reducer.py -input /user/hduser/tfidf/2-word-count/* -output /user/hduser/tfidf/3-word-freq-in-corpus`
