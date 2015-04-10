echo `hadoop fs -rm /user/hduser/tfidf/2-word-count/*`
echo `hadoop fs -rmdir /user/hduser/tfidf/2-word-count`

echo `hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper job2/mapper.py -reducer job2/reducer.py -input /user/hduser/tfidf/1-word-freq/* -output /user/hduser/tfidf/2-word-count`
