shopt -s extglob
echo rm -rf !(build|build.sh|apidoc)

rm -rf build/website
make -C build/ html
cp -r apidoc build/website/html/