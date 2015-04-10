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

echo `hadoop fs -rm /user/hduser/tfidf/4-tfidf/*`
echo `hadoop fs -rmdir /user/hduser/tfidf/4-tfidf`

echo `hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper job4/mapper.py -input /user/hduser/tfidf/3-word-freq-in-corpus/* -output /user/hduser/tfidf/4-tfidf`
