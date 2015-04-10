#!/bin/bash
# check for arg
if [ $# -eq 0 ]
  then
    echo "Please give number of documents"
    exit
fi

re='^[0-9]+$'
if ! [[ $1 =~ $re ]] ; then
   echo "error: Argument not a number" >&2; exit 1
fi

DOCS=$1
export DOCS

# run job1
echo `hadoop fs -rm /user/hduser/tfidf/1-word-freq/*`
echo `hadoop fs -rmdir /user/hduser/tfidf/1-word-freq`

echo `hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper job1/mapper.py -reducer job1/reducer.py -input /user/hduser/tfidf/books/* -output /user/hduser/tfidf/1-word-freq`

# run job2
echo `hadoop fs -rm /user/hduser/tfidf/2-word-count/*`
echo `hadoop fs -rmdir /user/hduser/tfidf/2-word-count`

echo `hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper job2/mapper.py -reducer job2/reducer.py -input /user/hduser/tfidf/1-word-freq/* -output /user/hduser/tfidf/2-word-count`

# run job3
echo `hadoop fs -rm /user/hduser/tfidf/3-word-freq-in-corpus/*`
echo `hadoop fs -rmdir /user/hduser/tfidf/3-word-freq-in-corpus`

echo `hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper job3/mapper.py -reducer job3/reducer.py -input /user/hduser/tfidf/2-word-count/* -output /user/hduser/tfidf/3-word-freq-in-corpus`

# run job4
echo `hadoop fs -rm /user/hduser/tfidf/4-tfidf/*`
echo `hadoop fs -rmdir /user/hduser/tfidf/4-tfidf`

echo `hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper job4/mapper.py -input /user/hduser/tfidf/3-word-freq-in-corpus/* -output /user/hduser/tfidf/4-tfidf`
