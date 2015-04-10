echo `hadoop fs -rm /user/hduser/tfidf/1-word-freq/*`
echo `hadoop fs -rmdir /user/hduser/tfidf/1-word-freq`

echo `hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper job1/mapper.py -reducer job1/reducer.py -input /user/hduser/tfidf/text* -output /user/hduser/tfidf/1-word-freq`
