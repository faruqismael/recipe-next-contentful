import Link from "next/link";
import ContentfulImage from "@/components/Contentfulimage";

const Recipecard = ({ recipe }) => {
  const { title, timetocook, thumbnails, slug } = recipe.fields;
  return (
    <>
      <Link href={`/${slug}`} aria-label={title}>
        <div>
          <ContentfulImage
            src={thumbnails?.fields.file.url}
            width={thumbnails?.fields.file.details.image.width}
            height={thumbnails?.fields.file.details.image.height}
            quality="100"
            alt={title}
          />
          <h2>{title}</h2>
          <span>Time taken: {timetocook} minutes</span>
        </div>
      </Link>
    </>
  );
};

export default Recipecard;
