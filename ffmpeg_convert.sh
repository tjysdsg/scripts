src_ext=$1
dst_ext=$2

for f in *.${src_ext}; do
    filename=$(basename -- "$f")
    filename="${filename%.*}"
    ffmpeg -i $f $filename.${dst_ext} || exit 1
done
