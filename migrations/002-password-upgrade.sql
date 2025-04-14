-- Note: This is just schema preparation. The actual password upgrade will happen 
-- gradually through the application code when users log in successfully.

-- Add a column to track if passwords have been upgraded
ALTER TABLE users ADD COLUMN IF NOT EXISTS pwd_version TEXT;

-- Update existing records to mark them as legacy
UPDATE users SET pwd_version = 'legacy' WHERE pwd_version IS NULL;

-- Create an index to help with password version queries
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_users_pwd_version ON users (pwd_version);

-- Add a comment to help future developers
COMMENT ON COLUMN users.pwd_version IS 'Tracks password hash version. NULL/legacy = MD5, v2 = PBKDF2-SHA256';